# SHOP MINHSANG - Cấu trúc dự án

## Cách chạy
```bash
# Cài thư viện
pip install -r requirements.txt

# Cấu hình môi trường
cp .env.example .env
# Chỉnh sửa .env với BOT_TOKEN và ADMIN_TELEGRAM_ID của bạn

# Chạy web + bot
python app.py
```

## Cấu trúc file

```
📁 project/
├── app.py              # ⭐ File chạy chính
├── config.py           # Cấu hình, VIP, thao tác DB
├── algorithms.py       # Thuật toán dự đoán Tài/Xỉu (~4300 dòng)
├── predict.py          # Hàm analyze, predict, lịch sử (~1400 dòng)
├── templates.py        # HTML templates (~2600 dòng)
├── routes.py           # Flask routes/endpoints (~600 dòng)
├── telegram_bot.py     # Telegram Bot handlers (~1200 dòng)
├── requirements.txt    # Thư viện cần cài
├── .env.example        # Mẫu file cấu hình
├── data.json           # Database người dùng (tự tạo)
├── history.json        # Lịch sử kết quả game (tự tạo)
├── prediction_history.json  # Lịch sử dự đoán (tự tạo)
└── cau_history.json    # Lịch sử phân tích cầu (tự tạo)
```

## Luồng dữ liệu

```
app.py
 ├── config.py      ← cấu hình chung
 ├── algorithms.py  ← thuật toán
 ├── predict.py     ← dùng algorithms
 ├── templates.py   ← HTML
 ├── routes.py      ← dùng predict + templates + config
 └── telegram_bot.py← dùng config
```

## Biến môi trường (.env)

| Biến | Mô tả |
|------|-------|
| BOT_TOKEN | Token Telegram bot |
| ADMIN_TELEGRAM_ID | Telegram ID của admin |
| PORT | Cổng web (mặc định: 5000) |
| SECRET_KEY | Khóa bảo mật session |
