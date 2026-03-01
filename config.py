# -*- coding: utf-8 -*-
# ================== config.py ==================
# Cấu hình chung, VIP, và thao tác với database

import os, json, time, hashlib, subprocess, sys, threading
from dotenv import load_dotenv
from nanoid import generate

load_dotenv()

# ================== CONFIG ==================
BOT_TOKEN   = os.getenv("BOT_TOKEN", "8297499534:AAGUPJfvoaxsCmbC-SnjIMxf5nm2vnNxlNA")
ADMIN_ID    = int(os.getenv("ADMIN_TELEGRAM_ID", "7219600109"))
PORT        = int(os.getenv("PORT", os.getenv("FLASK_PORT", "5000")))
SECRET_KEY  = os.getenv("SECRET_KEY", "minhsang_shop_secret_2024_xK9p")
SHOP_NAME   = "SHOP MINHSANG"
# FIX: Dùng thư mục chứa file thực thi để đảm bảo đúng đường dẫn trên mọi môi trường
_BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
DATA_FILE   = os.path.join(_BASE_DIR, "data.json")

# ================== VIP LEVELS CONFIG ==================
VIP_LEVELS = {
    "Đồng":        {"history_depth": 500,   "exp_required": 0,     "benefits": "Lịch sử 500 phiên",                           "color": "#CD7F32", "icon": "🥉"},
    "Bạc":         {"history_depth": 1000,  "exp_required": 100,   "benefits": "Lịch sử 1000 phiên",                          "color": "#C0C0C0", "icon": "🥈"},
    "Vàng":        {"history_depth": 2000,  "exp_required": 500,   "benefits": "Lịch sử 2000 phiên, Phân tích nâng cao",      "color": "#FFD700", "icon": "🥇"},
    "Kim Cương":   {"history_depth": 5000,  "exp_required": 2000,  "benefits": "Lịch sử 5000 phiên, AI ưu tiên",             "color": "#B9F2FF", "icon": "💎"},
    "Huyền Thoại": {"history_depth": 10000, "exp_required": 10000, "benefits": "Lịch sử 10000 phiên, Thuật toán độc quyền",  "color": "#FF6B6B", "icon": "👑"},
}

def get_vip_level(exp):
    levels = ["Đồng", "Bạc", "Vàng", "Kim Cương", "Huyền Thoại"]
    for level in reversed(levels):
        if exp >= VIP_LEVELS[level]["exp_required"]:
            return level
    return "Đồng"

def get_history_depth(vip_level):
    return VIP_LEVELS.get(vip_level, VIP_LEVELS["Đồng"])["history_depth"]

# ================== DATABASE ==================
DB_LOCK = threading.Lock()

def load_db():
    default_db = {
        "shop_keys": [], "users": {}, "active": {},
        "blocked_web_login": [], "transactions": [],
        "blocked_telegram_ids": [], "cau_history": {}
    }
    with DB_LOCK:
        if not os.path.exists(DATA_FILE):
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                json.dump(default_db, f, indent=2, ensure_ascii=False)
            return default_db
        try:
            with open(DATA_FILE, encoding="utf-8") as f:
                data = json.load(f)
                if not isinstance(data, dict):
                    raise ValueError("Dữ liệu hỏng")
                for k, v in default_db.items():
                    if k not in data:
                        data[k] = v
                return data
        except Exception as e:
            print(f"⚠️ Lỗi đọc data.json: {e}. Đang tạo lại file mới...")
            try:
                os.rename(DATA_FILE, f"{DATA_FILE}.bak.{int(time.time())}")
            except: pass
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                json.dump(default_db, f, indent=2, ensure_ascii=False)
            return default_db

def save_db(db):
    with DB_LOCK:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(db, f, indent=2, ensure_ascii=False)

def hash_password(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

def create_key(kind="LK", days=None, price=0):
    code = f"{kind}-{generate(size=8).upper()}"
    now = time.time()
    expires = None if days is None else now + days * 86400
    return {
        "code": code, "type": kind, "price": price,
        "createdAt": now, "expiresAt": expires,
        "status": "available", "usedBy": None
    }

# ================== SHARED STATE ==================
pending_deposits = {}
deposit_counter = 0
bot_app = None
