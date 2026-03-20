# -*- coding: utf-8 -*-
# ================== intrusion_detector.py ==================
# Phát hiện & ghi log kẻ tấn công tự động (bot, scraper, brute-force)
# Thu thập: IP, User-Agent, headers, tần suất request
# Gửi cảnh báo về Telegram admin

import os, json, time, re
from collections import defaultdict
from flask import request

# ================== CẤU HÌNH ==================
# Số request tối đa trong TIME_WINDOW giây trước khi bị coi là tấn công
RATE_LIMIT        = 30        # requests
TIME_WINDOW       = 60        # giây
BAN_DURATION      = 3600      # giây bị chặn (1 tiếng)
LOG_FILE          = os.path.join(os.path.dirname(os.path.abspath(__file__)), "intrusion_log.json")

# Route nhạy cảm - theo dõi kỹ hơn
SENSITIVE_ROUTES  = ["/api/", "/login", "/register", "/admin"]

# User-Agent của bot/scraper phổ biến
BOT_UA_PATTERNS   = [
    r"python-requests", r"curl/", r"wget/", r"scrapy",
    r"httpx", r"aiohttp", r"go-http-client", r"java/",
    r"libwww-perl", r"nikto", r"sqlmap", r"nmap",
    r"masscan", r"zgrab", r"dirbuster", r"gobuster",
    r"wfuzz", r"hydra", r"burpsuite", r"postman",
    r"insomnia", r"axios/0\.", r"okhttp",
]

# ================== BỘ NHỚ THEO DÕI ==================
_request_log  = defaultdict(list)   # ip → [timestamps]
_banned_ips   = {}                  # ip → ban_until timestamp
_attack_count = defaultdict(int)    # ip → tổng lần vi phạm

# ================== HÀM LẤY IP THỰC ==================
def get_real_ip():
    """Lấy IP thực, xử lý cả proxy/CDN"""
    # Cloudflare
    cf_ip = request.headers.get("CF-Connecting-IP")
    if cf_ip:
        return cf_ip.strip()
    # Nginx / Load balancer
    forwarded = request.headers.get("X-Forwarded-For", "")
    if forwarded:
        return forwarded.split(",")[0].strip()
    real_ip = request.headers.get("X-Real-IP", "")
    if real_ip:
        return real_ip.strip()
    return request.remote_addr or "unknown"


def get_device_info():
    """Thu thập thông tin thiết bị/trình duyệt từ headers"""
    ua = request.headers.get("User-Agent", "N/A")
    return {
        "ip":           get_real_ip(),
        "user_agent":   ua,
        "accept_lang":  request.headers.get("Accept-Language", "N/A"),
        "accept":       request.headers.get("Accept", "N/A"),
        "referer":      request.headers.get("Referer", "N/A"),
        "origin":       request.headers.get("Origin", "N/A"),
        "method":       request.method,
        "path":         request.path,
        "query":        request.query_string.decode("utf-8", errors="replace"),
        "content_type": request.headers.get("Content-Type", "N/A"),
        "host":         request.headers.get("Host", "N/A"),
        "time":         time.strftime("%d/%m/%Y %H:%M:%S"),
        "timestamp":    time.time(),
    }


def is_bot_ua(ua: str) -> bool:
    """Phát hiện User-Agent của bot/tool tấn công"""
    ua_lower = ua.lower()
    for pattern in BOT_UA_PATTERNS:
        if re.search(pattern, ua_lower, re.IGNORECASE):
            return True
    return False


# ================== RATE LIMITING ==================
def check_rate_limit(ip: str) -> bool:
    """
    Trả về True nếu IP vượt quá giới hạn request.
    Tự động dọn dẹp log cũ.
    """
    now = time.time()
    # Giữ chỉ các request trong TIME_WINDOW
    _request_log[ip] = [t for t in _request_log[ip] if now - t < TIME_WINDOW]
    _request_log[ip].append(now)
    return len(_request_log[ip]) > RATE_LIMIT


def is_banned(ip: str) -> bool:
    """Kiểm tra IP có đang bị cấm không"""
    if ip in _banned_ips:
        if time.time() < _banned_ips[ip]:
            return True
        else:
            del _banned_ips[ip]  # Hết hạn ban
    return False


def ban_ip(ip: str):
    """Cấm IP trong BAN_DURATION giây"""
    _banned_ips[ip] = time.time() + BAN_DURATION
    _attack_count[ip] += 1


# ================== GHI LOG ==================
def save_intrusion_log(info: dict, reason: str):
    """Lưu log tấn công vào file JSON"""
    try:
        logs = []
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                logs = json.load(f)
    except Exception:
        logs = []

    entry = {**info, "reason": reason, "attack_count": _attack_count[info["ip"]]}
    logs.insert(0, entry)
    logs = logs[:500]   # Giữ tối đa 500 bản ghi

    try:
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            json.dump(logs, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"[INTRUSION LOG ERROR] {e}")


# ================== GỬI CẢNH BÁO TELEGRAM ==================
def send_telegram_alert(info: dict, reason: str):
    """Gửi cảnh báo về bot Telegram của admin"""
    try:
        from config import BOT_TOKEN, ADMIN_ID
        import requests as req

        attack_no = _attack_count[info["ip"]]
        msg = (
            f"🚨 PHÁT HIỆN TẤN CÔNG!\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"⚠️ Lý do: {reason}\n"
            f"🔢 Lần tấn công: #{attack_no}\n\n"
            f"📡 IP: {info['ip']}\n"
            f"🌐 Host: {info['host']}\n"
            f"🔗 Route: {info['method']} {info['path']}\n"
            f"❓ Query: {info['query'] or 'N/A'}\n\n"
            f"💻 Thiết bị:\n"
            f"   User-Agent: {info['user_agent'][:100]}\n"
            f"   Ngôn ngữ: {info['accept_lang']}\n"
            f"   Origin: {info['origin']}\n"
            f"   Referer: {info['referer']}\n\n"
            f"🕐 Thời gian: {info['time']}\n"
            f"⏳ Đã chặn IP trong 1 tiếng"
        )

        req.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={"chat_id": ADMIN_ID, "text": msg},
            timeout=5
        )
    except Exception as e:
        print(f"[INTRUSION ALERT ERROR] {e}")


# ================== HÀM XỬ LÝ CHÍNH ==================
def detect_and_block():
    """
    Gọi trong before_request. Trả về response 403 nếu phát hiện tấn công,
    None nếu bình thường.
    """
    from flask import jsonify

    # Bỏ qua ping/webhook nội bộ
    skip_paths = ["/ping", "/api/sepay-webhook"]
    if request.path in skip_paths:
        return None

    ip   = get_real_ip()
    info = get_device_info()
    ua   = info["user_agent"]
    reason = None

    # 1. Kiểm tra IP đang bị cấm
    if is_banned(ip):
        save_intrusion_log(info, "IP bị cấm - tiếp tục truy cập")
        return jsonify({
            "ok": False,
            "error": "tuổi đéll mà đòi lấy 🖕 IP của mày đã bị chặn.",
            "code": 403
        }), 403

    # 2. Phát hiện User-Agent bot/tool
    if is_bot_ua(ua):
        reason = f"Bot/Tool UA: {ua[:80]}"

    # 3. Rate limiting
    if not reason and check_rate_limit(ip):
        reason = f"Rate limit vượt {RATE_LIMIT} req/{TIME_WINDOW}s"

    # 4. Không có User-Agent (thường là script tự động)
    if not reason and (not ua or ua == "N/A"):
        reason = "Không có User-Agent"

    # 5. Nếu phát hiện → cấm + log + cảnh báo
    if reason:
        ban_ip(ip)
        save_intrusion_log(info, reason)
        send_telegram_alert(info, reason)
        print(f"[BLOCKED] {ip} | {reason}")
        return jsonify({
            "ok": False,
            "error": "tuổi đéll mà đòi lấy 🖕",
            "code": 403
        }), 403

    return None


# ================== ĐĂNG KÝ VÀO FLASK APP ==================
def register_intrusion_detector(app):
    """
    Gọi trong app.py:
        from intrusion_detector import register_intrusion_detector
        register_intrusion_detector(app)
    """
    @app.before_request
    def intrusion_check():
        return detect_and_block()

    print("[SECURITY] Intrusion Detector đã kích hoạt ✅")
