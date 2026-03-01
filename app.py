# -*- coding: utf-8 -*-
# ================== app.py ==================
# File chạy chính - khởi động Flask web + Telegram bot

import os, sys, subprocess, threading, asyncio

def install(package):
    print(f"⏳ Đang tự động cài đặt thư viện: {package}...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Auto-install thư viện cần thiết
REQUIRED_PACKAGES = [
    ("requests", "requests"),
    ("flask", "flask"),
    ("flask-cors", "flask_cors"),
    ("python-dotenv", "dotenv"),
    ("nanoid", "nanoid"),
    ("python-telegram-bot", "telegram")
]

for package, module in REQUIRED_PACKAGES:
    try:
        __import__(module)
        # Kiểm tra kỹ hơn cho telegram bot (cần bản v20+)
        if module == "telegram":
            from telegram.ext import Application
    except ImportError:
        install(package)
    except Exception as e:
        print(f"⚠️ Lỗi kiểm tra thư viện {package}: {e}")
        install(package)

from flask import Flask
from flask_cors import CORS
from config import SECRET_KEY, PORT
from predict import load_history, load_prediction_history, load_cau_history
from routes import register_routes

# ================== KHỞI TẠO FLASK ==================
app = Flask(__name__)
app.secret_key = SECRET_KEY
CORS(app)

# Đăng ký tất cả routes
register_routes(app)

# ================== CHẠY CHƯƠNG TRÌNH ==================
if __name__ == "__main__":
    try:
        print("[START] Đang khởi động SHOP MINHSANG...")

        # Tải lịch sử
        load_history()
        load_prediction_history()
        load_cau_history()
        print("[OK] Đã tải lịch sử dự đoán và phân tích cầu")

        # Khởi động Telegram bot trong thread riêng
        try:
            from telegram_bot import run_bot_in_thread, TELEGRAM_AVAILABLE
            if TELEGRAM_AVAILABLE:
                bot_thread = threading.Thread(target=run_bot_in_thread, daemon=True)
                bot_thread.start()
                print("[OK] Bot Telegram đang chạy song song")
            else:
                print("[INFO] Telegram bot bị tắt - chỉ chạy web server")
        except Exception as e:
            print(f"[WARNING] Không thể khởi động bot: {e}")
            print("[INFO] Website vẫn hoạt động bình thường")

        print(f"[START] Flask chạy tại http://0.0.0.0:{PORT}")
        app.run(host="0.0.0.0", port=PORT, debug=False, use_reloader=False)
    except Exception as e:
        print(f"\n❌ LỖI SERVER NGHIÊM TRỌNG: {e}")
        print("👉 Vui lòng chụp ảnh màn hình lỗi này và gửi cho admin.")
        input("Nhấn Enter để thoát...")
