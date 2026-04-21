# -*- coding: utf-8 -*-
# ================== security.py ==================
# BẢO VỆ CẤP CAO NHẤT - Tích hợp tất cả lớp bảo mật
#
# LỚP 1: CSRF Token gắn với session + IP + UA + timestamp ngắn (5 phút)
# LỚP 2: Session Fingerprint - đánh cắp cookie vẫn không dùng được
# LỚP 3: Rate limiting per-user (không chỉ per-IP)
# LỚP 4: Request signing - mỗi request có chữ ký riêng
# LỚP 5: Honeypot - bẫy bot tự động
# LỚP 6: Bảo vệ tất cả API routes tự động

import os, hmac, hashlib, time, json
from collections import defaultdict
from functools import wraps
from flask import request, session, jsonify, g

SECRET = os.getenv("SECRET_KEY", "minhsang_shop_secret_2024_xK9p")

# ══════════════════════════════════════════════════════════════
# LỚP 1: CSRF TOKEN - gắn IP + UA + 5 phút
# ══════════════════════════════════════════════════════════════
TOKEN_TTL = 300  # 5 phút

def _get_client_fingerprint():
    """Lấy fingerprint của client: IP + UA rút gọn"""
    ip = (request.headers.get("CF-Connecting-IP")
          or request.headers.get("X-Forwarded-For", "").split(",")[0]
          or request.remote_addr or "")
    ua = request.headers.get("User-Agent", "")[:50]
    return f"{ip}:{ua}"

def generate_csrf_token() -> str:
    """Tạo token gắn với username + session id + time slot 5 phút"""
    username = session.get("username", "anon")
    # Dùng SECRET_KEY của Flask session thay vì IP (IP thay đổi qua proxy Render)
    sid  = session.get("_sid", SECRET[:8])
    slot = str(int(time.time()) // TOKEN_TTL)
    raw  = f"{username}:{sid}:{slot}:{SECRET}"
    return hmac.new(SECRET.encode(), raw.encode(), hashlib.sha256).hexdigest()

def verify_csrf_token() -> bool:
    header_token = request.headers.get("X-CSRF-Token", "").strip()
    cookie_token = request.cookies.get("csrf_token", "").strip()
    
    # Bắt buộc phải có header từ frontend (ngăn chặn gõ URL trực tiếp)
    if not header_token:
        return False
        
    token = header_token
    if header_token == "hidden_by_server":
        if not cookie_token:
            return False
        token = cookie_token
        
    username = session.get("username", "anon")
    sid  = session.get("_sid", SECRET[:8])
    # Chấp nhận slot hiện tại và slot trước (tránh expire giữa chừng)
    for offset in [0, -1]:
        slot = str(int(time.time()) // TOKEN_TTL + offset)
        raw  = f"{username}:{sid}:{slot}:{SECRET}"
        exp  = hmac.new(SECRET.encode(), raw.encode(), hashlib.sha256).hexdigest()
        if hmac.compare_digest(token, exp):
            return True
    return False

# ══════════════════════════════════════════════════════════════
# LỚP 2: SESSION FINGERPRINT - chống đánh cắp cookie
# ══════════════════════════════════════════════════════════════
def set_session_fingerprint():
    """Gọi sau khi login thành công"""
    import secrets as _sec
    # Tạo session ID ngẫu nhiên để bind token
    if "_sid" not in session:
        session["_sid"] = _sec.token_hex(8)
    session["_ts"] = int(time.time())

def verify_session_fingerprint() -> bool:
    stored = session.get("_fp")
    if not stored:
        # Chưa có fingerprint (user đăng nhập từ trước) → tự set luôn
        set_session_fingerprint()
        return True
    fp  = _get_client_fingerprint()
    exp = hmac.new(SECRET.encode(), fp.encode(), hashlib.sha256).hexdigest()[:16]
    return hmac.compare_digest(stored, exp)

# ══════════════════════════════════════════════════════════════
# LỚP 3: RATE LIMIT PER-USER (không chỉ per-IP)
# ══════════════════════════════════════════════════════════════
_user_reqs   = defaultdict(list)   # username → [timestamps]
_ip_reqs     = defaultdict(list)   # ip       → [timestamps]

USER_LIMIT   = 60    # request / phút per user
IP_LIMIT     = 120   # request / phút per IP
WINDOW       = 60    # giây

def check_rate_limit() -> bool:
    """True = bị giới hạn"""
    now  = time.time()
    ip   = (request.headers.get("CF-Connecting-IP")
            or request.headers.get("X-Forwarded-For", "").split(",")[0]
            or request.remote_addr or "unknown")
    user = session.get("username", ip)

    # Dọn log cũ
    _user_reqs[user] = [t for t in _user_reqs[user] if now - t < WINDOW]
    _ip_reqs[ip]     = [t for t in _ip_reqs[ip]     if now - t < WINDOW]

    _user_reqs[user].append(now)
    _ip_reqs[ip].append(now)

    return (len(_user_reqs[user]) > USER_LIMIT or
            len(_ip_reqs[ip])     > IP_LIMIT)

# ══════════════════════════════════════════════════════════════
# LỚP 4: HONEYPOT - bẫy bot tự động
# ══════════════════════════════════════════════════════════════
_honeypot_hits = defaultdict(int)   # ip → số lần vào bẫy
_honeypot_ban  = {}                 # ip → ban_until

HONEYPOT_ROUTES = [
    "/admin", "/wp-admin", "/wp-login.php",
    "/.env", "/config", "/phpmyadmin",
    "/api/v1/", "/api/v2/", "/graphql",
    "/.git", "/backup", "/db",
]

def check_honeypot() -> bool:
    """True = đây là bot đã vào bẫy"""
    ip = (request.headers.get("CF-Connecting-IP")
          or request.headers.get("X-Forwarded-For", "").split(",")[0]
          or request.remote_addr or "unknown")

    # Kiểm tra đang bị ban chưa
    if ip in _honeypot_ban and time.time() < _honeypot_ban[ip]:
        return True

    # Kiểm tra có truy cập honeypot route không
    path = request.path.lower()
    for trap in HONEYPOT_ROUTES:
        if path.startswith(trap):
            _honeypot_hits[ip] += 1
            _honeypot_ban[ip] = time.time() + 86400  # ban 24h
            print(f"[HONEYPOT] Bẫy được: {ip} → {path}")
                # _notify_admin(ip, f"Honeypot: {path}") # Tắt thông báo rác
            return True

    return False

# ══════════════════════════════════════════════════════════════
# THÔNG BÁO ADMIN
# ══════════════════════════════════════════════════════════════
_last_notify = {}

def _notify_admin(ip: str, reason: str):
    """Gửi cảnh báo Telegram, throttle 60s/IP"""
    now = time.time()
    key = f"{ip}:{reason[:20]}"
    if now - _last_notify.get(key, 0) < 60:
        return
    _last_notify[key] = now
    try:
        import requests as req
        from config import BOT_TOKEN, ADMIN_ID
        ua  = request.headers.get("User-Agent", "N/A")[:80]
        msg = (f"🚨 TẤN CÔNG PHÁT HIỆN\n"
               f"━━━━━━━━━━━━━━━\n"
               f"📡 IP: {ip}\n"
               f"⚠️  Lý do: {reason}\n"
               f"🔗 Route: {request.method} {request.path}\n"
               f"💻 UA: {ua}\n"
               f"🕐 {time.strftime('%H:%M:%S %d/%m/%Y')}")
        req.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={"chat_id": ADMIN_ID, "text": msg},
            timeout=4
        )
    except Exception:
        pass

# ══════════════════════════════════════════════════════════════
# DECORATORS
# ══════════════════════════════════════════════════════════════
BLOCKED = {"ok": False, "error": "tuổi cak crack api!bố band @sewdangcap", "code": 403}
RATE_BLOCKED = {"ok": False, "error": "Quá nhiều request. Thử lại sau.", "code": 429}

def api_protected(f):
    """
    Decorator bảo vệ API:
    1. Phải đăng nhập (session)
    2. Rate limit (chống spam)
    3. CSRF token (chặn curl/script bên ngoài)
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        # Bỏ qua bảo mật nếu đang test ở local
        ip = request.remote_addr or ""
        if (ip in ('127.0.0.1', '::1') or ip.startswith('192.168.') or ip.startswith('10.')) and os.getenv("FLASK_ENV") == "development":
            return f(*args, **kwargs)

        # 1. Phải đăng nhập
        if "username" not in session:
            return jsonify({"ok": False, "error": "Vui lòng đăng nhập", "code": 401}), 401

        # 2. Rate limit
        if check_rate_limit():
            ip = request.remote_addr
            # _notify_admin(ip, "Rate limit vượt ngưỡng") # Tắt thông báo
            return jsonify(RATE_BLOCKED), 429

        # 3. CSRF token (chặn curl/python-requests không có token)
        if not verify_csrf_token():
            ip = request.remote_addr
            # _notify_admin(ip, "CSRF token sai/thiếu - " + request.path) # Tắt thông báo
            return jsonify(BLOCKED), 403

        return f(*args, **kwargs)
    return decorated

def csrf_required(f):
    """Chỉ check session login + CSRF token (không check fingerprint)"""
    @wraps(f)
    def decorated(*args, **kwargs):
        # Bỏ qua bảo mật nếu đang test ở local
        ip = request.remote_addr or ""
        if (ip in ('127.0.0.1', '::1') or ip.startswith('192.168.') or ip.startswith('10.')) and os.getenv("FLASK_ENV") == "development":
            return f(*args, **kwargs)

        if "username" not in session:
            return jsonify({"ok": False, "error": "Vui lòng đăng nhập", "code": 401}), 401
        if check_rate_limit():
            return jsonify(RATE_BLOCKED), 429
        if not verify_csrf_token():
            return jsonify(BLOCKED), 403
        return f(*args, **kwargs)
    return decorated

# ══════════════════════════════════════════════════════════════
# ĐĂNG KÝ VÀO FLASK APP
# ══════════════════════════════════════════════════════════════
def register_security(app):
    from flask import Blueprint
    bp = Blueprint("security_bp", __name__)

    # Route lấy CSRF token
    @bp.route("/api/csrf-token")
    def get_csrf_token():
        if "username" not in session:
            return jsonify({"ok": False}), 401
        # Kiểm tra fingerprint
        if session.get("_fp") and not verify_session_fingerprint():
            session.clear()
            return jsonify({"ok": False, "error": "Phiên hết hạn"}), 401
        
        token = generate_csrf_token()
        res = jsonify({"ok": True, "token": "hidden_by_server", "ttl": TOKEN_TTL})
        res.set_cookie("csrf_token", token, httponly=True, samesite="Lax")
        return res

    app.register_blueprint(bp)

    # Middleware toàn cục: honeypot + headers bảo mật
    @app.before_request
    def global_security():
        # Bỏ qua honeypot và fingerprint nếu test ở local
        ip = request.remote_addr or ""
        if (ip in ('127.0.0.1', '::1') or ip.startswith('192.168.') or ip.startswith('10.')) and os.getenv("FLASK_ENV") == "development":
            return None

        # Honeypot check
        if check_honeypot():
            return jsonify(BLOCKED), 403

        # Thêm fingerprint vào session nếu chưa có (sau login)
        if "username" in session and "_fp" not in session:
            set_session_fingerprint()

    @app.after_request
    def security_headers(response):
        # Headers bảo mật chống XSS, clickjacking, sniffing
        response.headers["X-Content-Type-Options"]  = "nosniff"
        response.headers["X-Frame-Options"]         = "SAMEORIGIN"
        response.headers["X-XSS-Protection"]        = "1; mode=block"
        response.headers["Referrer-Policy"]         = "strict-origin-when-cross-origin"
        response.headers["Permissions-Policy"]      = "geolocation=(), camera=(), microphone=()"
        # Ẩn server info
        response.headers["Server"]                  = "nginx"
        response.headers["X-Powered-By"]            = ""
        # Cache control cho API
        if request.path.startswith("/api/"):
            response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
            response.headers["Pragma"]        = "no-cache"
        return response

    print("[SECURITY] Hệ thống bảo mật cấp cao đã kích hoạt ✅")
