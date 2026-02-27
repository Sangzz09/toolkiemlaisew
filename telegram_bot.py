# -*- coding: utf-8 -*-
# ================== telegram_bot.py ==================
# Telegram Bot - tất cả handlers và lệnh

import os, json, time, asyncio, threading
from datetime import datetime
from config import BOT_TOKEN, ADMIN_ID, SHOP_NAME, load_db, save_db, create_key, get_vip_level, VIP_LEVELS

try:
    from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
    from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler
    TELEGRAM_AVAILABLE = True
except ImportError:
    TELEGRAM_AVAILABLE = False

async def log_all_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"[DEBUG] log_all_messages được gọi!")
    if update.message:
        user = update.effective_user
        msg_text = update.message.text or "[No text]"
        print(
            f"📨 Message từ {user.username or user.first_name} (ID: {user.id}): {msg_text}"
        )

        # Check if user is banned from Telegram bot
        db = load_db()
        if user.id in db.get("blocked_telegram_ids", []):
            await update.message.reply_text(
                "⛔ Tài khoản của bạn đã bị chặn bot.")
            return

        if msg_text and "TÔI ĐÃ CHUYỂN KHOẢN" in msg_text.upper():
            user_id = user.id
            user_telegram = user.username or user.first_name
            user_fullname = user.first_name + (f" {user.last_name}"
                                               if user.last_name else "")

            found_deposit = None
            deposit_key_to_remove = None
            for deposit_id, deposit in pending_deposits.items():
                if deposit["user_id"] == user_id:
                    found_deposit = deposit
                    deposit_key_to_remove = deposit_id
                    break

            if found_deposit:
                admin_msg = (
                    f"✅ XÁC NHẬN CHUYỂN KHOẢN (Telegram)\n\n"
                    f"👤 Tên: {user_fullname}\n"
                    f"📱 Telegram: @{user_telegram} (ID: {user_id})\n"
                    f"🎮 Tài khoản: {found_deposit['username']}\n"
                    f"💵 Số tiền: {found_deposit['amount']:,}đ\n\n"
                    f"💬 User đã xác nhận chuyển khoản!\n\n"
                    f"Duyệt: /duyet {found_deposit['username']}")

                try:
                    await context.bot.send_message(chat_id=ADMIN_ID,
                                                   text=admin_msg)
                    await update.message.reply_text(
                        f"✅ Đã nhận xác nhận!\n\n"
                        f"📱 Admin sẽ kiểm tra và duyệt nạp tiền cho bạn trong giây lát.\n\n"
                        f"⏳ Vui lòng đợi...")
                    # Remove the deposit after confirmation to avoid duplicate processing
                    if deposit_key_to_remove:
                        del pending_deposits[deposit_key_to_remove]
                except Exception as e:
                    print(f"Lỗi gửi thông báo admin: {e}")
            else:
                await update.message.reply_text(
                    f"❌ Không tìm thấy yêu cầu nạp tiền!\n\n"
                    f"Vui lòng gửi lệnh /nap trước khi xác nhận chuyển khoản.")
        else:
            # Trả lời cho tất cả tin nhắn khác
            await update.message.reply_text(
                "👋 Xin chào! Tôi là bot của SHOP MINHSANG.\n\n"
                "📋 Để xem các lệnh, gửi /help\n"
                "🎰 Để nạp tiền, gửi /nap <username> <số_tiền>")
    elif update.edited_message:
        print(f"✏️ Edited message received")
    else:
        print(f"📥 Update received: {update}")


async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_id = update.effective_user.id
        username = update.effective_user.username or update.effective_user.first_name
        print(f"📥 Nhận lệnh /start từ user: {username} (ID: {user_id})")

        # Tin nhắn chào mừng chung
        msg = (f"👋 Xin chào {username}!\n"
               f"🎰 chào mừng bạn đến với shop minhsang\n"
               f"🌐 web hỗ trợ anh em nhiệt tình\n"
               f"🔑 key giá rẻ học sinh\n"
               f"💬 liên hệ admin @sewdangcap\n\n")

        # Nếu là Admin thì hiện thêm danh sách lệnh quản lý
        if user_id == ADMIN_ID:
            msg += ("👑 MENU ADMIN:\n"
                    "/duyet <username> - Duyệt nạp tiền\n"
                    "/menu - Menu admin\n"
                    "/key <1d|1t|vv> - Tạo key\n"
                    "/list - Danh sách key\n"
                    "/block <key> - Khóa key\n"
                    "/band <username> - Khóa web\n"
                    "/unband <username> - Mở khóa web\n"
                    "/ban_tg <id> - Chặn bot\n"
                    "/unban_tg <id> - Bỏ chặn bot\n"
                    "/xoa <username> - Xóa user\n"
                    "/tong - Thống kê\n"
                    "/lichsu <game> - Xem lịch sử")
        else:
            # Nếu là User thường thì hiện hướng dẫn cơ bản
            msg += ("📋 HƯỚNG DẪN SỬ DỤNG:\n"
                    "1️⃣ Gửi /nap <user> <số tiền> để nạp tiền\n"
                    "2️⃣ Gửi /help để xem hướng dẫn chi tiết\n"
                    "3️⃣ Truy cập Website để sử dụng Tool AI")

        # Tạo nút bấm liên hệ Admin
        keyboard = [
            [
                InlineKeyboardButton("💬 Liên hệ Admin", url="https://t.me/sewdangcap"),
                InlineKeyboardButton("🌐 Truy cập Website", url="https://google.com")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(msg, reply_markup=reply_markup)
        print(f"✅ Đã gửi /start reply cho user {username}")
    except Exception as e:
        print(f"❌ Lỗi trong cmd_start: {str(e)}")
        import traceback
        traceback.print_exc()


async def cmd_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 HƯỚNG DẪN SỬ DỤNG:\n\n"
        "1️⃣ Gửi lệnh nạp tiền:\n   /nap <tên_tài_khoản> <số_tiền>\n   Ví dụ: /nap Minhsang 100000\n\n"
        "2️⃣ Chuyển khoản theo thông tin:\n   - Ngân hàng: MB Bank\n   - STK: 0886027767\n   - Tên: TRAN MINH SANG\n   - Nội dung: NAP <tên_tài_khoản>\n\n"
        "3️⃣ Sau khi chuyển khoản xong, nhắn:\n   TÔI ĐÃ CHUYỂN KHOẢN\n\n"
        "4️⃣ Admin sẽ duyệt và cộng tiền\n\n"
        "💬 Hỗ trợ: @minhsangdangcap")


async def callback_approve_deposit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Xử lý khi admin click button duyệt nạp tiền"""
    query = update.callback_query
    print(f"[DEBUG] callback_approve_deposit được gọi! callback_data: {query.data}")
    
    # Kiểm tra xem người click có phải admin không
    print(f"[DEBUG] User ID: {query.from_user.id}, ADMIN_ID: {ADMIN_ID}")
    if query.from_user.id != ADMIN_ID:
        print(f"[DEBUG] ❌ User không phải admin!")
        await query.answer("❌ Bạn không có quyền duyệt!", show_alert=True)
        return
    
    # Lấy short_id từ callback_data
    short_id = query.data.replace("approve_", "")
    print(f"[DEBUG] short_id: {short_id}")
    print(f"[DEBUG] pending_deposits keys: {list(pending_deposits.keys())}")
    
    if short_id not in pending_deposits:
        print(f"[DEBUG] ❌ short_id không tìm thấy!")
        await query.answer("❌ Yêu cầu nạp tiền không còn hiệu lực!", show_alert=True)
        return
    
    deposit = pending_deposits[short_id]
    username = deposit["username"]
    amount = deposit["amount"]
    
    print(f"[DEBUG] Duyệt nạp tiền cho {username}: {amount}đ")
    
    # Duyệt nạp tiền
    db = load_db()
    if username not in db["users"]:
        print(f"[DEBUG] ❌ Tài khoản không tồn tại!")
        await query.answer("❌ Tài khoản không tồn tại!", show_alert=True)
        return
    
    # Cộng tiền cho user
    db["users"][username]["balance"] = db["users"][username].get("balance", 0) + amount
    print(f"[DEBUG] ✅ Đã cộng tiền. Số dư mới: {db['users'][username]['balance']}")
    
    # Ghi lại giao dịch
    transaction = {
        "username": username,
        "type": "deposit",
        "amount": amount,
        "time": time.time(),
        "method": "telegram_admin"
    }
    db["transactions"].append(transaction)
    save_db(db)
    
    # Cập nhật UI
    await query.answer(f"✅ Đã duyệt nạp {amount:,}đ cho {username}!", show_alert=True)
    
    # Sửa tin nhắn để hiển thị trạng thái đã duyệt
    await query.edit_message_text(
        f"✅ XÁC NHẬN CHUYỂN KHOẢN (Telegram)\n\n"
        f"🎮 Tài khoản: {username}\n"
        f"💵 Số tiền: {amount:,}đ\n\n"
        f"✅ ĐƠNHÀNG ĐÃ ĐƯỢC DUYỆT!")
    
    # Xóa yêu cầu nạp sau khi duyệt
    del pending_deposits[short_id]
    print(f"[DEBUG] ✅ Đã xóa pending_deposits[{short_id}]")



async def callback_confirm_transfer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Xử lý khi user click button xác nhận chuyển khoản"""
    query = update.callback_query
    print(f"[DEBUG] callback_confirm_transfer được gọi! callback_data: {query.data}")
    await query.answer()
    
    # Lấy deposit_id từ callback_data
    deposit_id = query.data.replace("confirm_transfer_", "")
    print(f"[DEBUG] deposit_id: {deposit_id}")
    print(f"[DEBUG] pending_deposits keys: {list(pending_deposits.keys())}")
    
    if deposit_id not in pending_deposits:
        print(f"[DEBUG] ❌ deposit_id không tìm thấy trong pending_deposits!")
        await query.edit_message_text("❌ Yêu cầu nạp tiền không còn hiệu lực!")
        return
    
    deposit = pending_deposits[deposit_id]
    user_id = deposit["user_id"]
    user_telegram = deposit["user_telegram"]
    user_fullname = deposit["user_fullname"]
    username = deposit["username"]
    amount = deposit["amount"]
    
    print(f"[DEBUG] Gửi message cho admin. ADMIN_ID: {ADMIN_ID}")
    
    # Gửi thông báo admin kèm button duyệt
    admin_msg = (
        f"✅ XÁC NHẬN CHUYỂN KHOẢN (Telegram)\n\n"
        f"👤 Tên: {user_fullname}\n"
        f"📱 Telegram: @{user_telegram} (ID: {user_id})\n"
        f"🎮 Tài khoản: {username}\n"
        f"💵 Số tiền: {amount:,}đ\n\n"
        f"💬 User đã xác nhận chuyển khoản!")
    
    # Tạo short ID để avoid callback_data quá dài (Telegram limit 64 bytes)
    global deposit_counter
    deposit_counter += 1
    short_id = f"d{deposit_counter}"
    pending_deposits[short_id] = deposit
    # Xóa cái deposit_id cũ để tránh duplicate
    del pending_deposits[deposit_id]
    print(f"[DEBUG] Tạo short_id {short_id} từ {deposit_id}")
    
    print(f"[DEBUG] Tạo button với callback_data: approve_{short_id}")
    admin_keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("✅ Duyệt nạp tiền", callback_data=f"approve_{short_id}")]
    ])
    
    try:
        print(f"[DEBUG] Đang gửi message tới admin...")
        await context.bot.send_message(chat_id=ADMIN_ID, text=admin_msg, reply_markup=admin_keyboard)
        print(f"[DEBUG] ✅ Message gửi thành công!")
        
        await query.edit_message_text(
            f"✅ Đã nhận xác nhận!\n\n"
            f"📱 Admin sẽ kiểm tra và duyệt nạp tiền cho bạn trong giây lát.\n\n"
            f"⏳ Vui lòng đợi...")
        # Không xóa pending_deposits ở đây - chỉ xóa sau khi admin duyệt
    except Exception as e:
        print(f"[ERROR] Lỗi gửi message: {e}")
        import traceback
        traceback.print_exc()
        await query.edit_message_text(f"❌ Lỗi: {str(e)}")


async def cmd_nap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_telegram = update.effective_user.username or update.effective_user.first_name
    user_fullname = update.effective_user.first_name + (
        f" {update.effective_user.last_name}"
        if update.effective_user.last_name else "")

    if len(context.args) < 2:
        await update.message.reply_text(
            "❌ Sai cú pháp!\n\nĐúng: /nap <tên_tài_khoản> <số_tiền>\nVí dụ: /nap Minhsang 100000")
        return

    username = context.args[0]
    try:
        amount = int(context.args[1])
        if amount <= 0:
            raise ValueError()
    except:
        await update.message.reply_text("❌ Số tiền không hợp lệ!")
        return

    db = load_db()
    if username not in db["users"]:
        await update.message.reply_text(
            f"❌ Tài khoản '{username}' không tồn tại!")
        return

    # Check if user is banned from Telegram bot
    if user_id in db.get("blocked_telegram_ids", []):
        await update.message.reply_text(
            "⛔ Tài khoản Telegram của bạn đã bị chặn bot.")
        return

    deposit_id = f"{user_id}_{int(time.time())}"
    pending_deposits[deposit_id] = {
        "user_id": user_id,
        "user_telegram": user_telegram,
        "user_fullname": user_fullname,
        "username": username,
        "amount": amount,
        "time": time.time()
    }

    # Debug log
    print(f"💰 Tạo yêu cầu nạp tiền mới:")
    print(f"  - Deposit ID: {deposit_id}")
    print(f"  - Username: {username}")
    print(f"  - Amount: {amount}")
    print(f"  - Pending deposits: {len(pending_deposits)} yêu cầu")

    admin_msg = (f"💰 YÊU CẦU NẠP TIỀN MỚI (Telegram)\n\n"
                 f"👤 Tên: {user_fullname}\n"
                 f"📱 Telegram: @{user_telegram} (ID: {user_id})\n"
                 f"🎮 Tài khoản game: {username}\n"
                 f"💵 Số tiền: {amount:,}đ\n"
                 f"🔑 ID: {deposit_id}\n\n"
                 f"⏳ Đang chờ user chuyển khoản...\n\n"
                 f"Duyệt: /duyet {username}")

    try:
        await context.bot.send_message(chat_id=ADMIN_ID, text=admin_msg)
        
        # Gửi thông tin và button xác nhận cho user
        msg = (f"✅ Đã gửi yêu cầu nạp tiền!\n\n"
               f"👤 Tài khoản: {username}\n"
               f"💵 Số tiền: {amount:,}đ\n\n"
               f"📋 THÔNG TIN CHUYỂN KHOẢN:\n"
               f"🏦 Ngân hàng: MB Bank\n"
               f"💳 STK: 0886027767\n"
               f"👤 Tên: TRAN MINH SANG\n"
               f"📝 Nội dung: NAP {username}\n\n"
               f"⏳ Sau khi chuyển khoản, bấm nút bên dưới:")
        
        # Tạo inline keyboard button
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("✅ Xác nhận đã chuyển khoản", callback_data=f"confirm_transfer_{deposit_id}")]
        ])
        
        await update.message.reply_text(msg, reply_markup=keyboard)
    except Exception as e:
        await update.message.reply_text(f"❌ Lỗi gửi thông báo: {str(e)}")


async def cmd_duyet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("⛔ Bạn không có quyền sử dụng lệnh này"
                                        )
        return

    if not context.args:
        await update.message.reply_text(
            "❌ Sai cú pháp!\n\nĐúng: /duyet <tên_tài_khoản>\nVí dụ: /duyet Minhsang")
        return

    username = context.args[0]
    found_deposit = None
    deposit_key = None

    # Debug: Show all pending deposits
    print(f"🔍 Tìm kiếm nạp tiền cho username: {username}")
    print(f"📋 Pending deposits hiện tại: {pending_deposits}")

    for key, deposit in pending_deposits.items():
        print(f"  - Checking: {deposit.get('username')} == {username}?")
        if deposit.get("username", "").lower() == username.lower():
            if found_deposit is None or deposit["time"] > found_deposit["time"]:
                found_deposit = deposit
                deposit_key = key
                print(f"  ✅ Found match!")

    if not found_deposit:
        # Show helpful error message
        pending_users = [
            d.get("username", "N/A") for d in pending_deposits.values()
        ]
        msg = f"❌ Không tìm thấy yêu cầu nạp tiền cho tài khoản '{username}'\n\n"
        if pending_users:
            msg += f"📋 Các yêu cầu đang chờ:\n" + "\n".join(
                [f"  • {u}" for u in pending_users])
        else:
            msg += "📋 Hiện không có yêu cầu nạp tiền nào đang chờ duyệt"
        await update.message.reply_text(msg)
        return

    db = load_db()
    if username not in db["users"]:
        await update.message.reply_text(
            f"❌ Tài khoản '{username}' không tồn tại!")
        return

    db["users"][username]["balance"] = db["users"][username].get(
        "balance", 0) + found_deposit["amount"]
    save_db(db)

    # Lưu lịch sử giao dịch
    if "transactions" not in db:
        db["transactions"] = []

    transaction = {
        "type": "deposit",
        "username": username,
        "amount": found_deposit['amount'],
        "time": time.time(),
        "status": "completed"
    }
    db["transactions"].append(transaction)
    save_db(db)

    # Remove the deposit from pending list after successful processing
    if deposit_key:
        del pending_deposits[deposit_key]

    # Format ngày giờ hiện tại
    now = datetime.now()
    ngay_gio = now.strftime("%d/%m/%Y %H:%M:%S")

    await update.message.reply_text(
        f"✅ ĐƠN DUYỆT TK{username.upper()} THÀNH CÔNG\n\n"
        f"💰 Số tiền: {found_deposit['amount']:,}đ\n"
        f"🕐 Ngày giờ: {ngay_gio}\n\n"
        f"📊 Chi tiết:\n"
        f"👤 Tên: {found_deposit.get('user_fullname', 'N/A')}\n"
        f"📱 Telegram: @{found_deposit['user_telegram']}\n"
        f"💵 Số dư mới: {db['users'][username]['balance']:,}đ")

    try:
        user_msg = (
            f"✅ NẠP TIỀN THÀNH CÔNG!\n\n"
            f"💵 Số tiền đã nạp: {found_deposit['amount']:,}đ\n"
            f"💰 Số dư hiện tại: {db['users'][username]['balance']:,}đ\n\n"
            f"🎉 Cảm ơn bạn đã sử dụng dịch vụ!")
        await context.bot.send_message(chat_id=found_deposit["user_id"],
                                       text=user_msg)
    except Exception as e:
        print(f"Không thể gửi thông báo cho user: {e}")


async def cmd_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("⛔ Bạn không có quyền sử dụng lệnh này")
        return
    await update.message.reply_text(
        "📋 Menu Admin:\n\n"
        "/key 1d - Tạo key 1 ngày\n"
        "/key 1t - Tạo key 1 tháng\n"
        "/key vv - Tạo key vĩnh viễn\n"
        "/list - Xem tất cả key\n"
        "/block <key> - Khóa key\n"
        "/duyet <username> - Duyệt nạp tiền\n"
        "/band <username> - Khóa đăng nhập web\n"
        "/unband <username> - Mở khóa đăng nhập web\n"
        "/ban_tg <user_id> - Chặn user Telegram\n"
        "/unban_tg <user_id> - Bỏ chặn user Telegram\n"
        "/xoa <username> - Xóa tài khoản user\n"
        "/tong - Thống kê tổng quan hệ thống\n"
        "/lichsu <game> - Lịch sử dự đoán từng game")


async def cmd_key(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if user_id != ADMIN_ID:
        await update.message.reply_text(
            "⛔ BẠN KHÔNG CÓ QUYỀN TẠO KEY!\n\n"
            f"❌ Chỉ admin (ID: {ADMIN_ID}) mới có thể tạo key.\n"
            f"📱 ID của bạn: {user_id}\n\n"
            "💬 Liên hệ admin để được hỗ trợ.")
        return

    if not context.args:
        await update.message.reply_text(
            "❌ Thiếu tham số\nVí dụ: /key 1d, /key 1t, /key vv")
        return

    arg = context.args[0].lower()  # Convert to lowercase for easier comparison
    days = None
    key_type_str = ""

    if arg.endswith("d"):
        try:
            days = int(arg[:-1])
            key_type_str = f"{days}d"
        except ValueError:
            await update.message.reply_text("❌ Định dạng số ngày không hợp lệ.")
            return
    elif arg.endswith("t"):
        try:
            months = int(arg[:-1])
            days = months * 30  # Approximate months to days
            key_type_str = f"{months}t"
        except ValueError:
            await update.message.reply_text(
                "❌ Định dạng số tháng không hợp lệ.")
            return
    elif arg == "vv":
        days = None
        key_type_str = "vv"
    else:
        await update.message.reply_text(
            "❌ Tham số không hợp lệ\nVí dụ: /key 1d, /key 1t, /key vv")
        return

    k = create_key("LK", days)
    db = load_db()
    db["shop_keys"].append(k)
    save_db(db)

    expires_str = "Vĩnh viễn" if days is None else f"{days} ngày"
    key_code = k['code']

    # Gửi thông báo với key có thể copy
    await update.message.reply_text(
        f"✅ KEY ĐÃ ĐƯỢC TẠO THÀNH CÔNG!\n\n"
        f"👑 Tạo bởi: Admin (ID: {ADMIN_ID})\n"
        f"🔑 Code: `{key_code}`\n"
        f"⏰ Thời hạn: {expires_str}\n\n"
        f"📋 Nhấn vào mã key bên trên để sao chép\n"
        f"💬 Hoặc copy thủ công: {key_code}",
        parse_mode='Markdown')


async def cmd_huykey(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if user_id != ADMIN_ID:
        await update.message.reply_text(
            "⛔ BẠN KHÔNG CÓ QUYỀN KHÓA KEY!\n\n"
            f"❌ Chỉ admin (ID: {ADMIN_ID}) mới có thể khóa key.\n"
            f"📱 ID của bạn: {user_id}\n\n"
            "💬 Liên hệ admin để được hỗ trợ.")
        return

    if not context.args:
        await update.message.reply_text(
            "❌ Thiếu tham số\nVí dụ: /huykey LK-ABC123XY")
        return

    key_code = context.args[0].upper()
    db = load_db()

    # Tìm key
    key_found = None
    for k in db["shop_keys"]:
        if k["code"].upper() == key_code:
            key_found = k
            break

    if not key_found:
        await update.message.reply_text(
            f"❌ Key '{key_code}' không tồn tại!")
        return

    if key_found["status"] == "blocked":
        await update.message.reply_text(
            f"⚠️ Key '{key_code}' đã bị khóa từ trước!")
        return

    # Khóa key
    key_found["status"] = "blocked"
    save_db(db)

    # Nếu key đang được sử dụng, cấm đăng nhập user
    if key_found.get("usedBy"):
        username = key_found["usedBy"]
        if username not in db["blocked_web_login"]:
            db["blocked_web_login"].append(username)
            save_db(db)
        blocked_msg = f"\n🚫 Đã chặn đăng nhập tài khoản '{username}' trên web"
    else:
        blocked_msg = ""

    await update.message.reply_text(
        f"✅ KEY ĐÃ ĐƯỢC KHÓA THÀNH CÔNG!\n\n"
        f"🔑 Code: `{key_code}`\n"
        f"📊 Trạng thái cũ: {key_found.get('status', 'N/A')}\n"
        f"❌ Trạng thái mới: blocked\n"
        f"👤 Được sử dụng bởi: {key_found.get('usedBy', 'Chưa sử dụng')}{blocked_msg}",
        parse_mode='Markdown')


async def cmd_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("⛔ Bạn không có quyền sử dụng lệnh này"
                                        )
        return

    db = load_db()
    if not db["shop_keys"]:
        await update.message.reply_text("📋 Chưa có key nào được tạo")
        return

    msg = "📋 DANH SÁCH KEY:\n\n"
    for idx, k in enumerate(db["shop_keys"], 1):
        # Icon trạng thái gọn
        if k["status"] == "blocked":
            status_icon = "🔴"
        elif k["status"] == "available":
            status_icon = "🟢"
        else:
            status_icon = "🟡"

        # Hết hạn gọn
        if k["expiresAt"] is None:
            exp = "♾️"
        else:
            exp = time.strftime("%d/%m", time.localtime(k["expiresAt"]))

        # User gọn
        used_by = k.get("usedBy", "-")

        # Format 1 dòng gọn
        msg += f"{idx}. {status_icon} {k['code']} | {exp} | {used_by}\n"

    msg += f"\n💡 Tổng: {len(db['shop_keys'])} key"
    await update.message.reply_text(msg)


async def cmd_block(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("⛔ Bạn không có quyền sử dụng lệnh này"
                                        )
        return

    if not context.args:
        await update.message.reply_text(
            "❌ Sai cú pháp!\n\nĐúng: /block <key_code>\nVí dụ: /block LK-ABC123")
        return

    key_code = context.args[0]
    db = load_db()
    found = None

    for k in db["shop_keys"]:
        if k["code"] == key_code:
            found = k
            break

    if not found:
        await update.message.reply_text(f"❌ Không tìm thấy key '{key_code}'")
        return

    if found["status"] == "blocked":
        await update.message.reply_text(
            f"⚠️ Key '{key_code}' đã bị khóa từ trước!")
        return

    found["status"] = "blocked"

    # Xóa key khỏi active để user phải nhập lại key
    username_to_remove = found.get("usedBy")
    if username_to_remove and username_to_remove in db["active"]:
        if db["active"][username_to_remove]["code"] == key_code:
            del db["active"][username_to_remove]

    save_db(db)

    msg = f"✅ Đã khóa key '{key_code}' thành công!"
    if username_to_remove:
        msg += f"\n\n👤 User '{username_to_remove}' sẽ phải nhập lại key khi vào game."

    await update.message.reply_text(msg)


async def cmd_band(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("⛔ Bạn không có quyền sử dụng lệnh này"
                                        )
        return

    if not context.args:
        await update.message.reply_text(
            "❌ Sai cú pháp!\n\nĐúng: /band <username>\nVí dụ: /band Minhsang")
        return

    username_to_block = context.args[0]
    db = load_db()

    if "blocked_web_login" not in db:
        db["blocked_web_login"] = []

    if username_to_block in db["blocked_web_login"]:
        await update.message.reply_text(
            f"⚠️ Tài khoản '{username_to_block}' đã bị khóa đăng nhập web từ trước."
        )
        return

    db["blocked_web_login"].append(username_to_block)
    save_db(db)

    await update.message.reply_text(
        f"✅ Đã khóa tài khoản '{username_to_block}' khỏi đăng nhập web.")


async def cmd_unband(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("⛔ Bạn không có quyền sử dụng lệnh này"
                                        )
        return

    if not context.args:
        await update.message.reply_text(
            "❌ Sai cú pháp!\n\nĐúng: /unband <username>\nVí dụ: /unband Minhsang")
        return

    username_to_unblock = context.args[0]
    db = load_db()

    if "blocked_web_login" not in db or username_to_unblock not in db[
            "blocked_web_login"]:
        await update.message.reply_text(
            f"❌ Tài khoản '{username_to_unblock}' không bị khóa đăng nhập web."
        )
        return

    db["blocked_web_login"].remove(username_to_unblock)
    save_db(db)

    await update.message.reply_text(
        f"✅ Đã mở khóa tài khoản '{username_to_unblock}' khỏi đăng nhập web.")


async def cmd_ban_tg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("⛔ Bạn không có quyền sử dụng lệnh này"
                                        )
        return

    if not context.args:
        await update.message.reply_text(
            "❌ Sai cú pháp!\n\nĐúng: /ban_tg <user_id>\nVí dụ: /ban_tg 123456789")
        return

    try:
        user_id_to_ban = int(context.args[0])
    except ValueError:
        await update.message.reply_text("❌ User ID không hợp lệ.")
        return

    db = load_db()
    if "blocked_telegram_ids" not in db:
        db["blocked_telegram_ids"] = []

    if user_id_to_ban in db["blocked_telegram_ids"]:
        await update.message.reply_text(
            f"⚠️ User ID {user_id_to_ban} đã bị chặn bot từ trước.")
        return

    db["blocked_telegram_ids"].append(user_id_to_ban)
    save_db(db)

    await update.message.reply_text(
        f"✅ Đã chặn User ID {user_id_to_ban} khỏi bot.")


async def cmd_unban_tg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("⛔ Bạn không có quyền sử dụng lệnh này"
                                        )
        return

    if not context.args:
        await update.message.reply_text(
            "❌ Sai cú pháp!\n\nĐúng: /unban_tg <user_id>\nVí dụ: /unban_tg 123456789")
        return

    try:
        user_id_to_unban = int(context.args[0])
    except ValueError:
        await update.message.reply_text("❌ User ID không hợp lệ.")
        return

    db = load_db()

    if "blocked_telegram_ids" not in db or user_id_to_unban not in db[
            "blocked_telegram_ids"]:
        await update.message.reply_text(
            f"❌ User ID {user_id_to_unban} không bị chặn bot.")
        return

    db["blocked_telegram_ids"].remove(user_id_to_unban)
    save_db(db)

    await update.message.reply_text(
        f"✅ Đã bỏ chặn User ID {user_id_to_unban} khỏi bot.")


async def cmd_tong(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("⛔ Bạn không có quyền sử dụng lệnh này"
                                        )
        return

    db = load_db()

    # Thống kê users
    total_users = len(db.get("users", {}))
    total_balance = sum(
        user.get("balance", 0) for user in db.get("users", {}).values())

    # Thống kê keys
    total_keys = len(db.get("shop_keys", []))
    active_keys_count = len(
        [k for k in db.get("shop_keys", []) if k.get("status") == "available"])
    used_keys_count = len(
        [k for k in db.get("shop_keys", []) if k.get("status") == "used"])
    blocked_keys_count = len(
        [k for k in db.get("shop_keys", []) if k.get("status") == "blocked"])

    # Thống kê keys đang hoạt động
    active_users_with_keys = len(db.get("active", {}))

    # Thống kê user bị khóa
    blocked_web_users = len(db.get("blocked_web_login", []))
    blocked_tg_users = len(db.get("blocked_telegram_ids", []))

    # Danh sách user và số dư
    user_list = ""
    for idx, (username,
              user_data) in enumerate(db.get("users", {}).items(), 1):
        balance = user_data.get("balance", 0)
        user_id = user_data.get("user_id", "N/A")
        created = time.strftime(
            "%d/%m/%y", time.localtime(user_data.get("created_at",
                                                     time.time())))

        # Kiểm tra key đang hoạt động
        has_active = "🟢" if username in db.get("active", {}) else "⚪"

        # Kiểm tra bị khóa
        is_blocked = "🔴" if username in db.get("blocked_web_login", []) else ""

        # Lấy thông tin key nếu có
        key_info = ""
        if username in db.get("active", {}):
            active_key = db["active"][username]
            if active_key.get("expiresAt") is None:
                key_info = " | ♾️ VV"
            elif active_key.get("expiresAt", 0) > time.time():
                expires = time.strftime(
                    "%d/%m", time.localtime(active_key["expiresAt"]))
                key_info = f" | 🔑 {expires}"

        user_list += f"{idx}. {has_active}{is_blocked} {username}{key_info}\n"
        user_list += f"   💰 {balance:,}đ | 🆔 {user_id} | 📅 {created}\n"

    msg = f"""📊 THỐNG KÊ HỆ THỐNG

👥 NGƯỜI DÙNG:
━━━━━━━━━━━━━━━━━━
• Tổng số: {total_users} user
• Tổng số dư: {total_balance:,}đ
• Đang có key: {active_users_with_keys} user
• Bị khóa web: {blocked_web_users} user
• Bị chặn bot: {blocked_tg_users} user

🔑 KEYS:
━━━━━━━━━━━━━━━━━━
• Tổng số: {total_keys} key
• Còn trống: {active_keys_count} key
• Đã dùng: {used_keys_count} key
• Bị khóa: {blocked_keys_count} key

📋 CHI TIẾT USERS:
━━━━━━━━━━━━━━━━━━
{user_list if user_list else "Chưa có user nào"}

💡 Chú thích:
🟢 = Có key hoạt động
⚪ = Chưa có key
🔴 = Bị khóa web
♾️ VV = Key vĩnh viễn
🔑 = Ngày hết hạn key"""

    await update.message.reply_text(msg, parse_mode='Markdown')


async def cmd_xoa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("⛔ Bạn không có quyền sử dụng lệnh này")
        return

    if not context.args:
        await update.message.reply_text(
            "❌ Sai cú pháp!\n\nĐúng: /xoa <username>\nVí dụ: /xoa Minhsang")
        return

    username_to_delete = context.args[0]
    db = load_db()

    if username_to_delete not in db.get("users", {}):
        await update.message.reply_text(
            f"❌ Tài khoản '{username_to_delete}' không tồn tại!")
        return

    # Lưu thông tin user trước khi xóa để hiển thị
    user_info = db["users"][username_to_delete]
    balance = user_info.get("balance", 0)
    user_id = user_info.get("user_id", "N/A")

    # Xóa user khỏi database
    del db["users"][username_to_delete]

    # Xóa khỏi active keys nếu có
    if username_to_delete in db.get("active", {}):
        del db["active"][username_to_delete]

    # Xóa khỏi blocked_web_login nếu có
    if username_to_delete in db.get("blocked_web_login", []):
        db["blocked_web_login"].remove(username_to_delete)

    # Xóa các giao dịch của user (tùy chọn - có thể giữ lại để lưu lịch sử)
    if "transactions" in db:
        db["transactions"] = [t for t in db["transactions"] if t.get("username") != username_to_delete]

    # Giải phóng các keys đã dùng bởi user này
    for key in db.get("shop_keys", []):
        if key.get("usedBy") == username_to_delete:
            key["usedBy"] = None
            key["status"] = "available"

    save_db(db)

    await update.message.reply_text(
        f"✅ ĐÃ XÓA TÀI KHOẢN THÀNH CÔNG!\n\n"
        f"👤 Username: {username_to_delete}\n"
        f"🆔 User ID: {user_id}\n"
        f"💰 Số dư đã mất: {balance:,}đ\n\n"
        f"🔄 Các keys của user này đã được giải phóng\n"
        f"🔄 User sẽ bị đăng xuất ngay lập tức và phải đăng ký lại")


async def cmd_lichsu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("⛔ Bạn không có quyền sử dụng lệnh này")
        return

    if not context.args:
        await update.message.reply_text(
            "❌ Sai cú pháp!\n\n"
            "Đúng: /lichsu <game>\n"
            "Ví dụ: /lichsu sun\n\n"
            "Game có sẵn: sun, hit, b52, sum, luck8, sicbo")
        return

    game = context.args[0].lower()

    if game not in ["sun", "hit", "b52", "sum", "luck8", "sicbo", "789", "68gb", "lc79"]:
        await update.message.reply_text(
            "❌ Game không hợp lệ!\n\n"
            "Game có sẵn: sun, hit, b52, sum, luck8, sicbo, 789, 68gb, lc79")
        return

    game_names = {
        "sun": "SunWin",
        "hit": "HitClub",
        "b52": "B52",
        "sum": "SumClub",
        "luck8": "Luck8",
        "sicbo": "Sicbo SunWin",
        "789": "789Club",
        "68gb": "68 Game Bài",
        "lc79": "LC79"
    }
    game_name = game_names[game]

    # Lấy dữ liệu trực tiếp từ API
    api_data = None
    if game == "sun":
        api_data = safe_json(API_SUN, timeout=5)
    elif game == "hit":
        api_data = safe_json(API_HIT)
    elif game == "sum":
        api_data = safe_json(API_SUM)
    elif game == "b52":
        a = safe_json(API_B52A)
        b = safe_json(API_B52B)
        api_data = b if b and (not a or int(b.get("Phien", 0)) >= int(a.get("Phien", 0))) else a
    elif game == "luck8":
        api_data = safe_json(API_LUCK8)
    elif game == "789":
        api_data = safe_json(API_789)
    elif game == "68gb":
        api_data = safe_json(API_68GB)
    elif game == "lc79":
        api_data = safe_json(API_LC79)

    if not api_data:
        await update.message.reply_text(
            f"❌ Không thể kết nối API {game_name}!\n\n"
            f"Vui lòng thử lại sau.")
        return

    # Lấy phiên hiện tại từ API
    if game == "sun":
        current_session = api_data.get("phien", "---")
        current_result = normalize(api_data.get("ket_qua"))
    elif game == "hit":
        current_session = api_data.get("phien", "---")
        current_result = normalize(api_data.get("ket_qua"))
    elif game == "sum":
        current_session = api_data.get("Phien") or api_data.get("phien_hien_tai", "---")
        current_result = normalize(api_data.get("Ket_qua"))
    elif game == "b52":
        current_session = api_data.get("Phien", "---")
        current_result = normalize(api_data.get("Ket_qua"))
    elif game == "luck8":
        current_session = api_data.get("phien", "---")
        current_result = normalize(api_data.get("ket_qua"))
    elif game == "789":
        current_session = api_data.get("phien", "---")
        current_result = normalize(api_data.get("ket_qua"))
    elif game == "68gb":
        current_session = api_data.get("phien", "---")
        current_result = normalize(api_data.get("ket_qua"))
    elif game == "lc79":
        current_session = api_data.get("phien", "---")
        current_result = normalize(api_data.get("ket_qua"))

    # Lấy thống kê từ PREDICTION_HISTORY
    history = list(PREDICTION_HISTORY[game])

    if not history:
        await update.message.reply_text(
            f"📊 THỐNG KÊ SHOP MINHSANG - {game_name.upper()}\n\n"
            f"❌ Chưa có dữ liệu dự đoán")
        return

    # Tính toán thống kê shop (tổng quan)
    total = len(history)
    correct = sum(1 for p in history if p.get("correct") == True)
    wrong = sum(1 for p in history if p.get("correct") == False)
    accuracy = round(correct / (correct + wrong) * 100, 2) if (correct + wrong) > 0 else 0

    # Thống kê 30 phiên gần nhất
    recent_30 = history[-30:] if len(history) >= 30 else history
    recent_30_correct = sum(1 for p in recent_30 if p.get("correct") == True)
    recent_30_wrong = sum(1 for p in recent_30 if p.get("correct") == False)
    recent_30_total = recent_30_correct + recent_30_wrong
    recent_30_accuracy = round(recent_30_correct / recent_30_total * 100, 2) if recent_30_total > 0 else 0

    # Hiển thị 10 phiên gần nhất chi tiết (phiên +1 để phù hợp với logic dự đoán)
    recent_10 = history[-10:] if len(history) >= 10 else history
    recent_detail = ""

    # Đếm thắng/thua trong 10 phiên
    win_count = 0
    lose_count = 0
    pending_count = 0

    for idx, p in enumerate(reversed(recent_10), 1):
        session_raw = p.get("session", "N/A")

        # Phiên hiển thị = phiên trong history (đã +1 khi lưu)
        session_display = session_raw

        prediction = p.get("prediction", "N/A")
        actual = p.get("actual")
        is_correct = p.get("correct")

        # Hiển thị kết quả rõ ràng
        if actual and actual in ["Tài", "Xỉu"]:
            actual_text = actual
        else:
            actual_text = "⏳"

        if is_correct == True:
            status = "✅ THẮNG"
            win_count += 1
        elif is_correct == False:
            status = "❌ THUA"
            lose_count += 1
        else:
            status = "⏳ CHỜ"
            pending_count += 1

        recent_detail += f"{idx}. {status}\n   Phiên #{session_display} | Dự đoán: {prediction} → Kết quả: {actual_text}\n"

    # Hiển thị phiên hiện tại từ API
    next_session = "---"
    if current_session != "---":
        try:
            next_session = str(int(current_session) + 1)
        except:
            next_session = current_session

    msg = f"""📊 THỐNG KÊ SHOP MINHSANG - {game_name.upper()}

📡 API: Phiên #{current_session} | KQ: {current_result or '⏳'}
🎯 Dự đoán cho: Phiên #{next_session}

━━━━━━━━━━━━━━━━━━
📈 TỔNG QUAN:
• Tổng phiên: {total}
• Đúng: {correct} | Tỷ lệ: {accuracy}%

📊 30 PHIÊN GẦN NHẤT:
• Độ chính xác: {recent_30_accuracy}%
• Đúng: {recent_30_correct}/{recent_30_total}

📋 10 PHIÊN GẦN NHẤT:
• ✅ Thắng: {win_count}
• ❌ Thua: {lose_count}
• ⏳ Chờ KQ: {pending_count}

━━━━━━━━━━━━━━━━━━
{recent_detail}
━━━━━━━━━━━━━━━━━━
💡 Tỷ lệ thắng 10 phiên: {round(win_count/(win_count+lose_count)*100, 1) if (win_count+lose_count) > 0 else 0}%"""

    await update.message.reply_text(msg)


async def start_bot_async():
    global bot_app

    if not TELEGRAM_AVAILABLE:
        print("❌ Telegram bot bị tắt do thiếu thư viện python-telegram-bot")
        return

    print(f"🤖 Starting Telegram Bot...")
    print(f"🔑 Bot Token: {BOT_TOKEN[:20]}...")
    print(f"👑 Admin ID: {ADMIN_ID}")

    try:
        bot_app = Application.builder().token(BOT_TOKEN).build()

        # Thêm command handlers TRƯỚC message handler để đảm bảo ưu tiên xử lý
        bot_app.add_handler(CommandHandler("start", cmd_start))
        print("✅ Đã đăng ký handler /start")
        bot_app.add_handler(CommandHandler("help", cmd_help))
        bot_app.add_handler(CommandHandler("nap", cmd_nap))
        bot_app.add_handler(CommandHandler("duyet", cmd_duyet))
        bot_app.add_handler(CommandHandler("menu", cmd_menu))
        bot_app.add_handler(CommandHandler("key", cmd_key))
        bot_app.add_handler(CommandHandler("huykey", cmd_huykey))
        bot_app.add_handler(CommandHandler("list", cmd_list))
        bot_app.add_handler(CommandHandler("block", cmd_block))
        bot_app.add_handler(CommandHandler("band", cmd_band))
        bot_app.add_handler(CommandHandler("unband", cmd_unband))
        bot_app.add_handler(CommandHandler("ban_tg", cmd_ban_tg))
        bot_app.add_handler(CommandHandler("unban_tg", cmd_unban_tg))
        bot_app.add_handler(CommandHandler("tong", cmd_tong))
        bot_app.add_handler(CommandHandler("xoa", cmd_xoa))
        bot_app.add_handler(CommandHandler("lichsu", cmd_lichsu))

        # Thêm callback handler cho button xác nhận chuyển khoản và duyệt đơn
        bot_app.add_handler(CallbackQueryHandler(callback_confirm_transfer, pattern="^confirm_transfer_"))
        bot_app.add_handler(CallbackQueryHandler(callback_approve_deposit, pattern="^approve_"))

        # Thêm message handler SAU command handlers với ưu tiên thấp hơn
        bot_app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND,
                                           log_all_messages),
                            group=1)

        print("✅ Đã đăng ký tất cả handlers")
        
        async with bot_app:
            await bot_app.initialize()
            print("✅ Bot đã initialize")
            
            await bot_app.start()
            print("✅ Bot đã start")

            bot_info = await bot_app.bot.get_me()
            print(f"✅ Bot kết nối thành công!")
            print(f"📱 Bot username: @{bot_info.username}")
            print(f"🆔 Bot ID: {bot_info.id}")
            print(f"📝 Bot name: {bot_info.first_name}")
            print(f"💬 Chat tại: https://t.me/{bot_info.username}")
            
            # Xóa webhook nếu có
            await bot_app.bot.delete_webhook(drop_pending_updates=True)
            print("✅ Bắt đầu polling...")

            await bot_app.updater.start_polling(allowed_updates=Update.ALL_TYPES, drop_pending_updates=True)
            print("✅ Bot đang lắng nghe tin nhắn!")

            # Keep running
            while True:
                await asyncio.sleep(1)

    except Exception as e:
        print(f"❌ Lỗi khi khởi động bot: {str(e)}")
        import traceback
        traceback.print_exc()
        print(
            f"⚠️ Vui lòng kiểm tra lại BOT_TOKEN trong file .env hoặc biến môi trường"
        )


def run_bot_in_thread():
    """Chạy bot trong thread riêng với event loop riêng"""
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(start_bot_async())
    except Exception as e:
        print(f"[ERROR] Bot error: {e}")
    finally:
        try:
            loop.close()
        except:
            pass
