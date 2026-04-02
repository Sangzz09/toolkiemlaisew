# Tóm tắt thay đổi - Tool Shop Web

## Ngày: 02/04/2026

### ✅ Task 1: Sửa logic key do Admin/Bot tạo
**Status**: ✅ Hoàn thành (Đã sẵn có)

**File**: `config.py`

**Mô tả**: Hàm `create_key()` đã đúng cách set:
```python
"status": "available"
"usedBy": None
```

**Chi tiết**: Khi bot tạo key qua `/key` command, key sẽ được lưu vào `db["shop_keys"]` với trạng thái sẵn sàng (available) và người dùng chưa được gán (usedBy: None).

---

### ✅ Task 2: Tích hợp HitClub Hũ + MD5 vào 1 game (có đổi bàn)
**Status**: ✅ Hoàn thành (Đã sẵn có)

**Files**: 
- `game_hit.html`
- `routes.py` (endpoint `/api/predict/hit`)

**Mô tả**: Game HitClub đã có tab chuyển bàn hoạt động hoàn chỉnh:
- Tab "🎲 Bàn MD5" (mặc định)
- Tab "🏺 Bàn Hũ" 
- Hàm `switchBan(ban)` xử lý chuyển đổi
- Routes tự động map: `hit` + `ban=hu` → `hit-hu`
- Hiển thị thông tin cược cho bàn Hũ

---

### ✅ Task 3: Tích hợp 68GB Bàn Xanh + Bàn Đỏ vào 1 game (có đổi bàn)
**Status**: ✅ Hoàn thành

**File**: `game_68gb.html`

**Thay đổi**:

1. **Thêm CSS cho tabs** (dòng ~551):
```css
/* Tab chọn bàn */
.ban-tabs{display:flex;gap:8px;justify-content:center;margin-bottom:14px}
.ban-tab{...}
.ban-tab.active{...}
```

2. **Thêm HTML wrapper với tabs** (sau header):
```html
<!-- Tab chọn bàn -->
<div class="wrapper" style="display:block;position:fixed;top:100px;left:50%;transform:translateX(-50%);z-index:100;max-width:400px;width:90%">
<div class="ban-tabs">
  <button class="ban-tab active" id="tabXanh" onclick="switchBan('xanh')">💚 Bàn Xanh</button>
  <button class="ban-tab" id="tabDo" onclick="switchBan('do')">❤️ Bàn Đỏ</button>
</div>
</div>
```

3. **Thêm biến và hàm JavaScript**:
   - `let currentBan='xanh'` - Bàn hiện tại (mặc định Xanh)
   - `function switchBan(ban)` - Hàm chuyển bàn
   - Cập nhật `refresh()` để gửi ban parameter: `/api/predict/68gb?ban=xanh|do`

4. **Cách hoạt động**:
   - Bàn Xanh (mặc định): `/api/predict/68gb?ban=xanh` → internal_game = `68gb`
   - Bàn Đỏ: `/api/predict/68gb?ban=do` → internal_game = `68gb-do`

---

### ✅ Task 4: Sửa logic cảnh cáo bảo mật (remove vulgar language)
**Status**: ✅ Hoàn thành

**File**: `protect.js`

**Thay đổi**:

1. **Console warning messages** (dòng ~87-89):
   
   **Cũ**:
   ```javascript
   _nat.warn('%c CÓ TRÌNH ĐÉO MÀ LẤY','...');
   _nat.warn('%c Mua key: t.me/sewdangcap','...');
   _nat.warn('%c MOI CODE PASTE/CHAY O DAY DEU BI CHAN & BAO CAO ADMIN','...');
   ```
   
   **Mới**:
   ```javascript
   _nat.warn('%c ⚠️ BẢO MẢN LẠP TRÌNH','...');
   _nat.warn('%c Lợi dụng tính năng lập trình của trình duyệt có thể vi phạm điều khoản dịch vụ','...');
   _nat.warn('%c Bất kỳ mã nào được thực thi trong đây sẽ bị chặn và báo cáo tới quản trị viên','...');
   ```

2. **Main intrusion warning message** (dòng ~70):
   
   **Cũ**:
   ```
   🛑 Phát hiện công cụ tấn công!
   Hành động của bạn đã bị ghi lại và báo cáo admin.
   Phiên đã bị hủy.
   ```
   
   **Mới**:
   ```
   🔒 Bảo mật: Hoạt động trái phép phát hiện
   Hành động của bạn đã được ghi lại và báo cáo với quản trị viên. 
   Phiên của bạn đã được hủy bỏ để bảo vệ tài khoản.
   ```

---

### ✅ Task 5: Cảnh báo khi xâm nhập API không có token + bấm F12
**Status**: ✅ Hoàn thành

**Files**: 
- `routes.py` (logout route + api_predict route + _alert_crack_attempt function)
- `protect.js` (đã có logic gửi logout?reason=devtools)

**Thay đổi**:

1. **Logout route - Phát hiện F12/DevTools** (dòng ~100-130):
   ```python
   @bp.route("/logout")
   def logout():
       username = session.get("username")
       reason = request.args.get("reason", "")
       
       # Phát hiện F12/DevTools và gửi cảnh báo Telegram
       if reason == "devtools":
           # Gửi Telegram alert với thông tin:
           # - Tài khoản
           # - IP
           # - User Agent
           # - Thời gian
   ```

2. **API error messages - Chuyên nghiệp hóa**:
   
   **Cũ**:
   ```
   "có trình đéo mà lấy 🖕 Mua key: t.me/sewdangcap"
   ```
   
   **Mới**:
   ```
   "Chưa đăng nhập. Vui lòng mua key tại t.me/sewdangcap"
   "Yêu cầu không hợp lệ. Vui lòng sử dụng ứng dụng chính thức."
   ```

3. **Cải thiện _alert_crack_attempt() function** (dòng ~705-730):
   - Thêm parameter `attack_type` để xác định loại tấn công
   - Thêm attack labels dictionary với mô tả chi tiết:
     - `no_session`: Không có phiên đăng nhập
     - `missing_token`: Thiếu CSRF Token
     - `unauthorized_api_call`: Gọi API không có CSRF Token
   - Telegram message chi tiết hơn với icon ⚠️ và hướng dẫn hành động

4. **Cập nhật api_predict calls**:
   ```python
   _alert_crack_attempt(None, request, game, "no_session")
   _alert_crack_attempt(username, request, game, "missing_token")
   ```

**Cảnh báo Telegram được gửi**:
- **F12 Detection**: Khi user bấm F12
  ```
  🔍 PHÁT HIỆN MỞ DEVTOOLS (F12)
  👤 Tài khoản: [username]
  📡 IP: [ip_address]
  💻 UA: [user_agent]
  🕐 [timestamp]
  ```

- **API Crack Attempt**: Khi API được gọi không hợp lệ
  ```
  🚨 PHÁT HIỆN CỐ GẮNG XÂM NHẬP API
  [loại tấn công]
  👤 Tài khoản: [username]
  🎮 Game: [game]
  📡 IP: [ip_address]
  💻 UA: [user_agent]
  ```

---

## Tóm tắt

| Task | File | Thay đổi | Status |
|------|------|----------|--------|
| 1 | config.py | Kiểm tra (OK) | ✅ |
| 2 | game_hit.html, routes.py | Kiểm tra (OK) | ✅ |
| 3 | game_68gb.html | Thêm tabs, CSS, JS | ✅ |
| 4 | protect.js | Thay đổi messages | ✅ |
| 5 | routes.py, protect.js | Thêm F12 detection + alerts | ✅ |

---

## Kiểm tra hoạt động

### 1. Game Switching (68GB)
```
Bấm: 💚 Bàn Xanh → API: /api/predict/68gb?ban=xanh
Bấm: ❤️ Bàn Đỏ   → API: /api/predict/68gb?ban=do
```

### 2. Security Messages
- Mở DevTools → Cảnh báo professional + Telegram alert  
- Paste code → Message: "Bất kỳ mã nào được thực thi trong đây sẽ bị chặn..."
- Gọi API không CSRF → Responsee message chuyên nghiệp

### 3. Telegram Alerts
- F12: `🔍 PHÁT HIỆN MỞ DEVTOOLS (F12)`
- API Crack: `🚨 PHÁT HIỆN CỐ GẮNG XÂM NHẬP API`

---

## Lưu ý
- Tất cả changes đã được test và hoạt động
- Messages sử dụng tiếng Việt chuyên nghiệp
- Telegram alerts được gửi tới ADMIN_ID trong config
