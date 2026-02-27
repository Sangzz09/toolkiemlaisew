# -*- coding: utf-8 -*-
# ================== templates.py ==================
# Tất cả HTML templates (render_template_string)

HTML_REGISTER = """<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>Đăng ký - SHOP MINHSANG</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Segoe UI',system-ui,-apple-system,BlinkMacSystemFont,sans-serif;background:linear-gradient(135deg,#0a1628 0%%,#0d1f36 50%%,#112a45 100%%);color:#fff;min-height:100vh;display:flex;align-items:center;justify-content:center;position:relative;overflow-x:hidden;padding:15px}
body::before{content:'';position:absolute;width:100%;height:100%;background:radial-gradient(circle at 20% 50%,rgba(0,230,180,0.08) 0%%,transparent 50%%),radial-gradient(circle at 80% 50%,rgba(0,180,230,0.08) 0%%,transparent 50%%);animation:pulse 8s ease-in-out infinite;pointer-events:none}
@keyframes pulse{0%%,100%%{opacity:1}50%%{opacity:0.6}}
.form-container{position:relative;width:100%;max-width:500px;z-index:1}
.form-box{position:relative;background:rgba(13,31,54,0.98);padding:40px 30px;border-radius:24px;box-shadow:0 20px 60px rgba(0,0,0,0.6),0 0 0 1px rgba(0,230,180,0.2);backdrop-filter:blur(20px);border:1px solid rgba(0,230,180,0.15)}
.form-box::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,transparent,#00e6b4,transparent);animation:shine 3s infinite}
@keyframes shine{0%%,100%%{opacity:0.3}50%%{opacity:1}}
.logo-container{text-align:center;margin-bottom:25px}
.logo-container img{width:100px;height:100px;border-radius:20px;object-fit:cover;box-shadow:0 10px 35px rgba(0,230,180,0.4);animation:float 3s ease-in-out infinite;border:3px solid rgba(0,230,180,0.3)}
@keyframes float{0%%,100%%{transform:translateY(0)}50%%{transform:translateY(-10px)}}
.shop-title{text-align:center;margin-bottom:10px;font-size:26px;background:linear-gradient(135deg,#00e6b4,#00b4d8);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;font-weight:bold;letter-spacing:2px;text-transform:uppercase}
.shop-subtitle{text-align:center;margin-bottom:25px;font-size:13px;color:rgba(255,255,255,0.6);letter-spacing:1px}
.divider{display:flex;align-items:center;margin:25px 0;color:rgba(255,255,255,0.5);font-size:14px;font-weight:600}
.divider::before,.divider::after{content:'';flex:1;height:1px;background:rgba(0,230,180,0.2)}
.divider::before{margin-right:15px}
.divider::after{margin-left:15px}
.error{background:rgba(255,80,80,0.15);padding:15px;border-radius:12px;margin-bottom:20px;text-align:center;border:1px solid rgba(255,80,80,0.3);color:#ff8888;font-size:14px;animation:slideIn 0.3s ease-out}
.success{background:rgba(0,230,180,0.15);padding:15px;border-radius:12px;margin-bottom:20px;text-align:center;border:1px solid rgba(0,230,180,0.3);color:#00e6b4;font-size:14px;animation:slideIn 0.3s ease-out}
@keyframes slideIn{from{opacity:0;transform:translateY(-10px)}to{opacity:1;transform:translateY(0)}}
.form-group{margin-bottom:20px;position:relative}
.form-group label{display:block;margin-bottom:8px;color:#00e6b4;font-weight:600;font-size:14px;display:flex;align-items:center;gap:6px}
.input-wrapper{position:relative;width:100%}
.input-icon{position:absolute;left:16px;top:50%%;transform:translateY(-50%%);font-size:20px;color:rgba(0,230,180,0.6);pointer-events:none;z-index:1}
.form-group input{width:100%;padding:15px 16px 15px 48px;border:2px solid rgba(0,230,180,0.2);border-radius:12px;font-size:16px;background:rgba(0,230,180,0.05);color:#fff;transition:all 0.3s;outline:none;-webkit-appearance:none;-moz-appearance:none;appearance:none}
.form-group input:focus{border-color:#00e6b4;background:rgba(0,230,180,0.1);box-shadow:0 0 20px rgba(0,230,180,0.2)}
.form-group input::placeholder{color:rgba(255,255,255,0.4)}
.form-group input:valid{border-color:rgba(0,230,180,0.4)}
.password-toggle{position:absolute;right:16px;top:50%%;transform:translateY(-50%%);cursor:pointer;font-size:20px;color:rgba(0,230,180,0.6);user-select:none;z-index:2;transition:all 0.3s}
.password-toggle:hover{color:#00e6b4}
.btn{width:100%;padding:16px;background:linear-gradient(135deg,#00e6b4,#00b4d8);border:none;border-radius:12px;font-size:17px;font-weight:bold;color:#0a1628;cursor:pointer;transition:all 0.3s;box-shadow:0 8px 20px rgba(0,230,180,0.3);text-transform:uppercase;letter-spacing:1px;margin-top:10px}
.btn:hover{transform:translateY(-2px);box-shadow:0 12px 30px rgba(0,230,180,0.5)}
.btn:active{transform:translateY(0);box-shadow:0 6px 15px rgba(0,230,180,0.3)}
.btn:disabled{opacity:0.6;cursor:not-allowed;transform:none}
.footer-link{text-align:center;margin-top:25px;padding-top:20px;border-top:1px solid rgba(0,230,180,0.1);font-size:14px}
.footer-link a{color:#00e6b4;text-decoration:none;transition:all 0.3s;font-weight:600}
.footer-link a:hover{color:#00b4d8;text-decoration:underline}
.password-strength{margin-top:8px;height:4px;background:rgba(255,255,255,0.1);border-radius:2px;overflow:hidden;display:none}
.password-strength-bar{height:100%;background:linear-gradient(90deg,#ff4444,#ffaa00,#00e6b4);transition:width 0.3s;width:0}
.password-hint{font-size:12px;color:rgba(255,255,255,0.5);margin-top:6px;display:none}
@media (max-width: 480px){
.form-box{padding:30px 20px;border-radius:20px}
.logo-container img{width:80px;height:80px;border-radius:16px}
.shop-title{font-size:22px;letter-spacing:1.5px}
.shop-subtitle{font-size:12px}
.form-group label{font-size:13px}
.form-group input{padding:14px 16px 14px 46px;font-size:15px}
.input-icon{font-size:18px;left:14px}
.password-toggle{font-size:18px;right:14px}
.btn{padding:14px;font-size:16px}
.divider{font-size:13px;margin:20px 0}
.footer-link{font-size:13px}
}
@media (min-width: 481px) and (max-width: 768px){
.form-box{padding:35px 25px}
.logo-container img{width:90px;height:90px}
.shop-title{font-size:24px}
}
@media (min-width: 769px){
.form-container{max-width:520px}
.form-box{padding:45px 35px}
}
</style>
</head>
<body>
<div class="form-container">
<div class="form-box">
<div class="logo-container">
<img src="https://i.postimg.cc/ZKnYHWZF/IMG-1622.jpg" alt="SHOP MINHSANG Logo">
</div>
<div class="shop-title">SHOP MINHSANG</div>
<div class="shop-subtitle">Hệ thống dự đoán AI Gaming</div>
<div class="divider">Tạo tài khoản mới</div>
{% if error %}<div class="error">❌ {{ error }}</div>{% endif %}
{% if success %}<div class="success">✅ {{ success }}</div>{% endif %}
<form method="post" id="registerForm">
<div class="form-group">
<label>👤 Tên đăng nhập</label>
<div class="input-wrapper">
<span class="input-icon">👤</span>
<input name="username" type="text" placeholder="Nhập tên đăng nhập..." required autofocus minlength="3" maxlength="20">
</div>
</div>
<div class="form-group">
<label>🔒 Mật khẩu</label>
<div class="input-wrapper">
<span class="input-icon">🔒</span>
<input name="password" id="password" type="password" placeholder="Nhập mật khẩu (tối thiểu 6 ký tự)..." required minlength="6" maxlength="50">
<span class="password-toggle" onclick="togglePassword('password')">👁️</span>
</div>
<div class="password-strength" id="passwordStrength">
<div class="password-strength-bar" id="passwordStrengthBar"></div>
</div>
<div class="password-hint" id="passwordHint">Mật khẩu cần ít nhất 6 ký tự</div>
</div>
<div class="form-group">
<label>🔐 Xác nhận mật khẩu</label>
<div class="input-wrapper">
<span class="input-icon">🔐</span>
<input name="password2" id="password2" type="password" placeholder="Nhập lại mật khẩu..." required minlength="6" maxlength="50">
<span class="password-toggle" onclick="togglePassword('password2')">👁️</span>
</div>
</div>
<button type="submit" class="btn" id="submitBtn">🎯 Đăng ký ngay</button>
</form>
<div class="footer-link">
<span style="color:rgba(255,255,255,0.6)">Đã có tài khoản? </span>
<a href="/login">Đăng nhập ngay</a>
</div>
</div>
</div>
<script>
function togglePassword(id) {
    const input = document.getElementById(id);
    const toggle = input.nextElementSibling;
    if (input.type === 'password') {
        input.type = 'text';
        toggle.textContent = '🙈';
    } else {
        input.type = 'password';
        toggle.textContent = '👁️';
    }
}

const passwordInput = document.getElementById('password');
const strengthBar = document.getElementById('passwordStrengthBar');
const strengthContainer = document.getElementById('passwordStrength');
const passwordHint = document.getElementById('passwordHint');

passwordInput.addEventListener('input', function() {
    const password = this.value;
    const length = password.length;
    
    if (length > 0) {
        strengthContainer.style.display = 'block';
        passwordHint.style.display = 'block';
    } else {
        strengthContainer.style.display = 'none';
        passwordHint.style.display = 'none';
        return;
    }
    
    let strength = 0;
    if (length >= 6) strength += 33;
    if (length >= 10) strength += 33;
    if (/[A-Z]/.test(password)) strength += 17;
    if (/[0-9]/.test(password)) strength += 17;
    
    strengthBar.style.width = strength + '%%';
    
    if (strength < 33) {
        passwordHint.textContent = '⚠️ Mật khẩu yếu - Cần ít nhất 6 ký tự';
        passwordHint.style.color = '#ff4444';
    } else if (strength < 66) {
        passwordHint.textContent = '✓ Mật khẩu trung bình';
        passwordHint.style.color = '#ffaa00';
    } else {
        passwordHint.textContent = '✓ Mật khẩu mạnh';
        passwordHint.style.color = '#00e6b4';
    }
});

document.getElementById('registerForm').addEventListener('submit', function(e) {
    const password = document.getElementById('password').value;
    const password2 = document.getElementById('password2').value;
    
    if (password !== password2) {
        e.preventDefault();
        alert('❌ Mật khẩu xác nhận không khớp!');
        return false;
    }
    
    if (password.length < 6) {
        e.preventDefault();
        alert('❌ Mật khẩu phải có ít nhất 6 ký tự!');
        return false;
    }
});
</script>
</body>
</html>"""

HTML_LOGIN = """<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Đăng nhập - SHOP MINHSANG</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Segoe UI',system-ui,-apple-system,sans-serif;background:linear-gradient(135deg,#0a1628 0%%,#0d1f36 50%%,#112a45 100%%);color:#fff;min-height:100vh;display:flex;align-items:center;justify-content:center;padding:20px;position:relative}
body::before{content:'';position:absolute;width:100%;height:100%;background:radial-gradient(circle at 30% 50%,rgba(0,230,180,0.08) 0%%,transparent 50%%);animation:pulse 6s ease-in-out infinite}
@keyframes pulse{0%%,100%%{opacity:1}50%%{opacity:0.5}}
.form-box{background:rgba(13,31,54,0.98);padding:35px;border-radius:20px;box-shadow:0 15px 40px rgba(0,0,0,0.6);width:90%;max-width:400px;border:1px solid rgba(0,230,180,0.25);backdrop-filter:blur(15px);position:relative;z-index:1}
.logo-container{text-align:center;margin-bottom:25px}
.logo-container img{width:90px;height:90px;border-radius:18px;object-fit:cover;border:3px solid rgba(0,230,180,0.4);box-shadow:0 8px 20px rgba(0,230,180,0.3);transition:transform 0.3s}
.logo-container img:hover{transform:scale(1.05)}
.shop-title{text-align:center;margin-bottom:30px;font-size:26px;background:linear-gradient(135deg,#00e6b4,#00b4d8);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-weight:bold;letter-spacing:1px}
.form-group{margin-bottom:20px;position:relative}
.form-group input{width:100%;padding:14px 14px 14px 45px;border:2px solid rgba(0,230,180,0.25);border-radius:12px;font-size:15px;background:rgba(0,230,180,0.08);color:#fff;outline:none;transition:all 0.3s}
.form-group input:focus{border-color:#00e6b4;background:rgba(0,230,180,0.15);box-shadow:0 0 15px rgba(0,230,180,0.2)}
.form-group input::placeholder{color:rgba(255,255,255,0.45)}
.input-icon{position:absolute;left:15px;top:50%%;transform:translateY(-50%%);font-size:20px;color:rgba(0,230,180,0.7);pointer-events:none}
.btn{width:100%;padding:15px;background:linear-gradient(135deg,#00e6b4,#00b4d8);border:none;border-radius:12px;font-size:17px;font-weight:bold;color:#0a1628;cursor:pointer;transition:all 0.3s;box-shadow:0 6px 18px rgba(0,230,180,0.35);text-transform:uppercase;letter-spacing:0.5px;margin-top:10px}
.btn:hover{transform:translateY(-2px);box-shadow:0 10px 25px rgba(0,230,180,0.5)}
.btn:active{transform:translateY(0)}
.error{background:rgba(255,80,80,0.18);padding:14px;border-radius:12px;margin-bottom:20px;text-align:center;border:1px solid rgba(255,80,80,0.35);color:#ff9999;font-size:14px}
.footer-link{text-align:center;margin-top:25px;padding-top:20px;border-top:1px solid rgba(0,230,180,0.15);font-size:14px}
.footer-link a{color:#00e6b4;text-decoration:none;font-weight:600;transition:all 0.3s}
.footer-link a:hover{color:#00b4d8;text-decoration:underline}
</style>
</head>
<body>
<div class="form-box">
<div class="logo-container">
<img src="https://i.postimg.cc/ZKnYHWZF/IMG-1622.jpg" alt="SHOP MINHSANG Logo">
</div>
<div class="shop-title">ĐĂNG NHẬP</div>
{% if error %}<div class="error">❌ {{ error }}</div>{% endif %}
<form method="post">
<div class="form-group">
<span class="input-icon">👤</span>
<input name="username" type="text" placeholder="Tên đăng nhập" required autofocus>
</div>
<div class="form-group">
<span class="input-icon">🔒</span>
<input name="password" type="password" placeholder="Mật khẩu" required>
</div>
<button type="submit" class="btn">Đăng nhập</button>
</form>
<div class="footer-link">
<span style="color:rgba(255,255,255,0.6)">Chưa có tài khoản? </span>
<a href="/register">Đăng ký ngay</a>
</div>
</div>
</body>
</html>"""

HTML_MENU = """<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SHOP MINHSANG - AI Gaming</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Segoe UI',system-ui,-apple-system,sans-serif;background:#0a1628;color:#fff;min-height:100vh;display:flex}
.menu-toggle{position:fixed;top:20px;left:20px;z-index:1001;width:50px;height:50px;background:linear-gradient(135deg,#00e6b4,#00b4d8);border:none;border-radius:12px;cursor:pointer;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;box-shadow:0 8px 20px rgba(0,230,180,0.4);transition:all 0.3s}
.menu-toggle:hover{transform:scale(1.05);box-shadow:0 12px 30px rgba(0,230,180,0.6)}
.menu-toggle span{width:28px;height:3px;background:#0a1628;border-radius:2px;transition:all 0.3s}
.menu-toggle.active span:nth-child(1){transform:rotate(45deg) translate(8px,8px)}
.menu-toggle.active span:nth-child(2){opacity:0}
.menu-toggle.active span:nth-child(3){transform:rotate(-45deg) translate(8px,-8px)}
.sidebar{width:280px;background:rgba(13,31,54,0.95);border-right:1px solid rgba(0,230,180,0.1);display:flex;flex-direction:column;position:fixed;height:100vh;overflow-y:auto;backdrop-filter:blur(20px);transform:translateX(-100%);transition:transform 0.3s ease;z-index:1000}
.sidebar.active{transform:translateX(0)}
.sidebar-overlay{position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.5);z-index:999;opacity:0;pointer-events:none;transition:opacity 0.3s}
.sidebar-overlay.active{opacity:1;pointer-events:auto}
.sidebar-header{padding:25px 20px;border-bottom:1px solid rgba(0,230,180,0.1);display:flex;align-items:center;gap:15px;margin-top:60px}
.logo{width:50px;height:50px;border-radius:14px;overflow:hidden;box-shadow:0 8px 20px rgba(0,230,180,0.3)}
.logo img{width:100%;height:100%;object-fit:cover}
.sidebar-header-text h3{font-size:20px;background:linear-gradient(135deg,#00e6b4,#00b4d8);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:3px}
.sidebar-header-text p{font-size:12px;color:rgba(255,255,255,0.5);letter-spacing:1px}
.balance-card{margin:20px;padding:20px;background:linear-gradient(135deg,rgba(0,230,180,0.1),rgba(0,180,230,0.1));border-radius:16px;border:1px solid rgba(0,230,180,0.2)}
.balance-label{font-size:12px;color:rgba(255,255,255,0.6);margin-bottom:8px;display:flex;align-items:center;gap:5px}
.balance-amount{font-size:24px;font-weight:bold;background:linear-gradient(135deg,#00e6b4,#00b4d8);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
{% if has_active_key %}
.key-activation-box{margin:20px;padding:20px;background:linear-gradient(135deg,rgba(0,230,180,0.1),rgba(0,180,230,0.1));border-radius:16px;border:1px solid rgba(0,230,180,0.3)}
.key-status{padding:12px;border-radius:10px;text-align:center;font-size:13px}
.key-status.active{background:rgba(0,230,180,0.15);border:1px solid rgba(0,230,180,0.3);color:#00e6b4}
{% endif %}
.nav-section{margin:20px 0}
.nav-title{padding:10px 20px;font-size:11px;color:rgba(255,255,255,0.4);font-weight:600;letter-spacing:1px;display:flex;align-items:center;gap:8px}
.nav-item{display:flex;align-items:center;gap:12px;padding:14px 20px;color:rgba(255,255,255,0.7);text-decoration:none;transition:all 0.3s;position:relative}
.nav-item:hover{background:rgba(0,230,180,0.1);color:#00e6b4}
.nav-item.active{background:rgba(0,230,180,0.15);color:#00e6b4;border-left:3px solid #00e6b4}
.badge{margin-left:auto;padding:3px 10px;background:#ffa500;color:#000;border-radius:6px;font-size:10px;font-weight:bold}
.badge.new{background:#00e6b4}
.main-content{margin-left:0;flex:1;padding:30px;padding-left:90px;overflow-y:auto;width:100%}
.game-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:30px;margin-top:40px}
.game-card{background:linear-gradient(145deg,rgba(13,31,54,0.95),rgba(17,42,69,0.95));border-radius:24px;padding:40px 30px;text-align:center;border:2px solid rgba(0,230,180,0.15);transition:all 0.5s ease;position:relative;overflow:hidden;cursor:pointer}
.game-card::before{content:'';position:absolute;top:-50%;left:-50%;width:200%;height:200%;background:linear-gradient(45deg,transparent,rgba(0,230,180,0.1),transparent);transform:rotate(45deg);transition:all 0.6s}
.game-card:hover::before{left:100%;top:100%}
.game-card:hover{transform:translateY(-12px) scale(1.02);border-color:#00e6b4;box-shadow:0 25px 50px rgba(0,230,180,0.4),0 0 30px rgba(0,230,180,0.2)}
.game-card .game-icon{margin-bottom:20px;transition:transform 0.4s}
.game-card:hover .game-icon{transform:scale(1.1) rotate(5deg)}
.game-card .game-icon img{border:3px solid rgba(0,230,180,0.3);transition:all 0.4s}
.game-card:hover .game-icon img{border-color:#00e6b4;box-shadow:0 8px 25px rgba(0,230,180,0.5)}
.game-card h3{font-size:26px;margin-bottom:15px;background:linear-gradient(135deg,#00e6b4,#00b4d8);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-weight:700;letter-spacing:1px}
.game-card p{color:rgba(255,255,255,0.7);font-size:15px;line-height:1.8;margin-bottom:25px;min-height:50px}
.game-btn{display:inline-block;padding:14px 35px;background:linear-gradient(135deg,#00e6b4,#00b4d8);color:#0a1628;text-decoration:none;border-radius:14px;font-weight:bold;font-size:16px;transition:all 0.3s;box-shadow:0 8px 20px rgba(0,230,180,0.35);position:relative;overflow:hidden}
.game-btn::before{content:'';position:absolute;top:0;left:-100%;width:100%;height:100%;background:rgba(255,255,255,0.2);transition:all 0.4s}
.game-btn:hover::before{left:100%}
.game-btn:hover{transform:scale(1.08);box-shadow:0 12px 35px rgba(0,230,180,0.6)}
.status-bar{background:rgba(13,31,54,0.9);padding:15px 20px;border-radius:16px;border:1px solid rgba(0,230,180,0.1);display:flex;align-items:center;gap:15px;margin-bottom:30px}
.status-indicator{width:12px;height:12px;background:#00e6b4;border-radius:50%;box-shadow:0 0 20px #00e6b4;animation:pulse-status 2s infinite}
@keyframes pulse-status{0%,100%{opacity:1;transform:scale(1)}50%{opacity:0.6;transform:scale(1.2)}}
.status-text{font-size:14px;color:rgba(255,255,255,0.8)}
.status-time{margin-left:auto;font-weight:bold;color:#00e6b4;font-size:18px}
@media(max-width:768px){
.game-grid{grid-template-columns:1fr}
.main-content{padding-left:30px}
}

.luck8-container{position:fixed;top:50%;left:50%;transform:translate(-50%,-50%);width:95%;max-width:500px;background:linear-gradient(145deg,rgba(10,25,47,0.95),rgba(15,35,60,0.95));backdrop-filter:blur(20px);border-radius:30px;padding:40px;border:2px solid rgba(79,195,247,0.3);box-shadow:0 20px 60px rgba(0,0,0,0.6),0 0 100px rgba(79,195,247,0.15);z-index:10}
.luck8-logo{font-size:32px;text-align:center;margin-bottom:15px;color:#4fc3f7;text-shadow:0 0 20px rgba(79,195,247,0.8),0 0 40px rgba(79,195,247,0.4);font-weight:700;letter-spacing:2px;animation:glowPulse 2s ease-in-out infinite}
@keyframes glowPulse{0%,100%{text-shadow:0 0 20px rgba(79,195,247,0.8),0 0 40px rgba(79,195,247,0.4)}50%{text-shadow:0 0 30px rgba(79,195,247,1),0 0 60px rgba(79,195,247,0.6)}}
.luck8-session{text-align:center;font-size:20px;color:#bbdefb;margin-bottom:20px;font-weight:500;padding:12px 20px;background:rgba(79,195,247,0.1);border-radius:12px;border:1px solid rgba(79,195,247,0.2)}
.luck8-session span{color:#4fc3f7;font-weight:bold;font-size:22px}
.luck8-prediction{text-align:center;font-size:18px;color:#fff;margin-bottom:35px;padding:15px;background:rgba(0,230,180,0.1);border-radius:12px;border:1px solid rgba(0,230,180,0.3)}
.luck8-prediction-label{color:#81d4fa;font-size:14px;margin-bottom:8px;text-transform:uppercase;letter-spacing:1px}
.luck8-prediction-value{font-size:28px;font-weight:bold;text-shadow:0 0 15px currentColor}
.luck8-circle-container{display:flex;justify-content:space-around;gap:40px;margin-bottom:35px}
.luck8-circle-wrap{flex:1;display:flex;justify-content:center}
.luck8-circle{width:140px;height:140px;border-radius:50%;display:flex;flex-direction:column;justify-content:center;align-items:center;background:linear-gradient(145deg,rgba(20,40,70,0.8),rgba(30,50,80,0.6));border:3px solid rgba(255,255,255,0.2);transition:all 0.5s cubic-bezier(0.4,0,0.2,1);position:relative;cursor:pointer;box-shadow:0 10px 30px rgba(0,0,0,0.4)}
.luck8-circle:hover{transform:translateY(-5px) scale(1.05);box-shadow:0 15px 40px rgba(0,0,0,0.6)}
.luck8-tai{border-color:#ff6b6b;background:linear-gradient(145deg,rgba(255,107,107,0.2),rgba(255,107,107,0.05))}
.luck8-xiu{border-color:#4db6ac;background:linear-gradient(145deg,rgba(77,182,172,0.2),rgba(77,182,172,0.05))}
.luck8-icon{font-size:48px;margin-bottom:10px;transition:all 0.4s ease;filter:drop-shadow(0 0 10px currentColor)}
.luck8-tai .luck8-icon{color:#ff6b6b}
.luck8-xiu .luck8-icon{color:#4db6ac}
.luck8-label{font-size:22px;font-weight:bold;margin-top:6px;letter-spacing:1px}
.luck8-tai .luck8-label{color:#ff7675;text-shadow:0 0 10px rgba(255,118,117,0.5)}
.luck8-xiu .luck8-label{color:#4dd0e1;text-shadow:0 0 10px rgba(77,208,225,0.5)}
.luck8-circle.blink{animation:pulseBlink 1s ease-in-out infinite}
@keyframes pulseBlink{0%,100%{transform:scale(1);box-shadow:0 0 0 0 rgba(255,255,255,0.6),0 10px 30px rgba(0,0,0,0.4)}50%{transform:scale(1.15);box-shadow:0 0 0 20px rgba(255,255,255,0),0 15px 50px rgba(0,0,0,0.6);filter:brightness(1.4) drop-shadow(0 0 20px currentColor)}}
.luck8-info-box{background:rgba(15,35,60,0.6);border-radius:18px;padding:20px;border:1px solid rgba(79,195,247,0.25);box-shadow:inset 0 2px 10px rgba(0,0,0,0.3)}
.luck8-info-row{display:flex;justify-content:space-between;align-items:center;padding:12px 0;border-bottom:1px solid rgba(255,255,255,0.1)}
.luck8-info-row:last-child{border-bottom:none}
.luck8-info-label{color:#81d4fa;font-size:15px;font-weight:500}
.luck8-info-value{color:#fff;font-size:15px;font-weight:bold}
</style>
</head>
<body>
<button class="menu-toggle" onclick="toggleMenu()">
<span></span>
<span></span>
<span></span>
</button>
<div class="sidebar-overlay" onclick="toggleMenu()"></div>
<div class="sidebar">
<div class="sidebar-header">
<div class="logo"><img src="https://i.postimg.cc/ZKnYHWZF/IMG-1622.jpg" alt="SHOP MINHSANG"></div>
<div class="sidebar-header-text">
<h3>SHOP MINHSANG</h3>
</div>
</div>
<div class="balance-card">
<div class="balance-label">💰 SỐ DƯ</div>
<div class="balance-amount">{{ "{:,}".format(balance) }}đ</div>
</div>
{% if has_active_key %}
<div class="key-activation-box">
<div class="key-status active">
✅ Key đang hoạt động<br>
Hết hạn: {{ key_expires }}
</div>
</div>
{% endif %}
<div class="nav-section">
<div class="nav-title">🧭 KHÁM PHÁ</div>
<a href="/menu" class="nav-item active"><span>🏠</span> Trang chủ</a>
<a href="/menu" class="nav-item"><span>🎮</span> Chơi game <span class="badge">HOT</span></a>
</div>
<div class="nav-section">
<div class="nav-title">🛒 GIAO DỊCH</div>
<a href="/buy-key" class="nav-item"><span>🔑</span> Mua key</a>
<a href="/deposit" class="nav-item"><span>💳</span> Nạp tiền <span class="badge new">NEW</span></a>
</div>
<div class="nav-section">
<div class="nav-title">👤 TÀI KHOẢN</div>
<a href="/account" class="nav-item"><span>👤</span> Thông tin</a>
<a href="/logout" class="nav-item"><span>🚪</span> Đăng xuất</a>
</div>
</div>
<div class="main-content">
<div class="status-bar">
<div class="status-indicator"></div>
<div class="status-text">ONLINE</div>
<div class="status-time" id="time">00:00</div>
</div>
<h1 style="font-size:32px;margin-bottom:10px;background:linear-gradient(135deg,#00e6b4,#00b4d8);-webkit-background-clip:text;-webkit-text-fill-color:transparent">🎮Dự Đoán AI - Tài Xỉu</h1>
<p style="color:rgba(255,255,255,0.5);margin-bottom:30px">Chọn game để bắt đầu dự đoán</p>
<div class="game-grid">
<a href="/game/sun" style="text-decoration:none">
<div class="game-card">
<div class="game-icon"><img src="https://i.postimg.cc/q7ybsvSb/IMG-1615.jpg" alt="SunWin" style="width:80px;height:80px;border-radius:12px;object-fit:cover;box-shadow:0 4px 12px rgba(0,230,180,0.3)"></div>
<h3>SunWin</h3>
<p>Dự đoán tài xỉu SunWin với độ chính xác cao, cập nhật realtime</p>
<span class="game-btn">Vào chơi</span>
</div>
</a>
<a href="/game/hit" style="text-decoration:none">
<div class="game-card">
<div class="game-icon"><img src="https://i.postimg.cc/66YHLSbG/IMG-1616.jpg" alt="HitClub" style="width:80px;height:80px;border-radius:12px;object-fit:cover;box-shadow:0 4px 12px rgba(0,230,180,0.3)"></div>
<h3>HitClub</h3>
<p>Thuật toán AI phân tích tài xỉu HitClub chuẩn xác</p>
<span class="game-btn">Vào chơi</span>
</div>
</a>
<a href="/game/b52" style="text-decoration:none">
<div class="game-card">
<div class="game-icon"><img src="https://i.postimg.cc/q7swtZCB/IMG-1617.jpg" alt="B52" style="width:80px;height:80px;border-radius:12px;object-fit:cover;box-shadow:0 4px 12px rgba(0,230,180,0.3)"></div>
<h3>B52</h3>
<p>Dự đoán B52 với công nghệ AI tiên tiến nhất</p>
<span class="game-btn">Vào chơi</span>
</div>
</a>
<a href="/game/sum" style="text-decoration:none">
<div class="game-card">
<div class="game-icon"><img src="https://i.postimg.cc/C1gt9QB0/IMG-1593.jpg" alt="SumClub" style="width:80px;height:80px;border-radius:12px;object-fit:cover;box-shadow:0 4px 12px rgba(0,230,180,0.3)"></div>
<h3>SumClub</h3>
<p>Phân tích tài xỉu SumClub chuyên nghiệp</p>
<span class="game-btn">Vào chơi</span>
</div>
</a>
<a href="/game/luck8" style="text-decoration:none">
<div class="game-card">
<div class="game-icon"><img src="https://i.postimg.cc/tg4Pgzzt/IMG-1702.jpg" alt="Luck8" style="width:80px;height:80px;border-radius:12px;object-fit:cover;box-shadow:0 4px 12px rgba(0,230,180,0.3)"></div>
<h3>Luck8</h3>
<p>Dự đoán Luck8 với AI độ chính xác cao</p>
<span class="game-btn">Vào chơi</span>
</div>
</a>
<a href="/game/sicbo" style="text-decoration:none">
<div class="game-card">
<div class="game-icon"><img src="https://i.postimg.cc/5tLC4p8q/IMG-2048.jpg" alt="Sicbo SunWin" style="width:80px;height:80px;border-radius:12px;object-fit:cover;box-shadow:0 4px 12px rgba(0,230,180,0.3)"></div>
<h3>Sicbo SunWin</h3>
<p>Dự đoán Sicbo SunWin với AI độ chính xác cao</p>
<span class="game-btn">Vào chơi</span>
</div>
</a>
<a href="/game/789" style="text-decoration:none">
<div class="game-card">
<div class="game-icon"><img src="https://i.postimg.cc/43HWjS37/789.webp" alt="789Club" style="width:80px;height:80px;border-radius:12px;object-fit:cover;box-shadow:0 4px 12px rgba(0,230,180,0.3)"></div>
<h3>789Club</h3>
<p>Dự đoán 789Club với thuật toán AI mới nhất</p>
<span class="game-btn">Vào chơi</span>
</div>
</a>
<a href="/game/68gb" style="text-decoration:none">
<div class="game-card">
<div class="game-icon"><img src="https://i.postimg.cc/zDQVG2DG/OIP.webp" alt="68 Game Bài" style="width:80px;height:80px;border-radius:12px;object-fit:cover;box-shadow:0 4px 12px rgba(0,230,180,0.3)"></div>
<h3>68 Game Bài</h3>
<p>Phân tích 68 Game Bài chuẩn xác</p>
<span class="game-btn">Vào chơi</span>
</div>
</a>
<a href="/game/lc79" style="text-decoration:none">
<div class="game-card">
<div class="game-icon"><img src="https://i.postimg.cc/vTSzPJnm/lc79.webp" alt="LC79" style="width:80px;height:80px;border-radius:12px;object-fit:cover;box-shadow:0 4px 12px rgba(0,230,180,0.3)"></div>
<h3>LC79</h3>
<p>Dự đoán LC79 với công nghệ AI mới nhất</p>
<span class="game-btn">Vào chơi</span>
</div>
</a>
</div>
</div>
<script>
function updateTime(){
let now=new Date();
let h=now.getHours().toString().padStart(2,'0');
let m=now.getMinutes().toString().padStart(2,'0');
let s=now.getSeconds().toString().padStart(2,'0');
document.getElementById('time').textContent=h+':'+m+':'+s;
}
setInterval(updateTime,1000);
updateTime();

function toggleMenu(){
document.querySelector('.sidebar').classList.toggle('active');
document.querySelector('.sidebar-overlay').classList.toggle('active');
document.querySelector('.menu-toggle').classList.toggle('active');
}
</script>
</body>
</html>"""

HTML_ACCOUNT = """<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Tài khoản - SHOP MINHSANG</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Segoe UI',system-ui,-apple-system,sans-serif;background:#0a1628;color:#fff;min-height:100vh;padding:20px}
.container{max-width:900px;margin:0 auto}
.header{display:flex;align-items:center;gap:15px;margin-bottom:30px}
.back-btn{font-size:28px;color:#00e6b4;text-decoration:none;transition:all 0.3s}
.back-btn:hover{transform:translateX(-5px)}
h1{background:linear-gradient(135deg,#00e6b4,#00b4d8);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
h2{color:#00e6b4;font-size:20px;margin:30px 0 15px}
.info-box{background:rgba(13,31,54,0.95);border-radius:20px;padding:30px;margin-bottom:20px;border:1px solid rgba(0,230,180,0.2);backdrop-filter:blur(20px)}
.info-item{display:flex;justify-content:space-between;padding:18px 0;border-bottom:1px solid rgba(255,255,255,0.1)}
.info-item:last-child{border-bottom:none}
.label{color:#00e6b4;font-weight:600}
.value{color:#fff;font-weight:500}
.history-box{background:rgba(13,31,54,0.95);border-radius:20px;padding:25px;border:1px solid rgba(0,230,180,0.2);backdrop-filter:blur(20px);margin-bottom:20px}
.transaction{display:flex;justify-content:space-between;align-items:center;padding:15px;background:rgba(0,230,180,0.05);border-radius:12px;margin-bottom:12px;border:1px solid rgba(0,230,180,0.1)}
.transaction:last-child{margin-bottom:0}
.trans-info{flex:1}
.trans-type{font-size:14px;color:#00e6b4;font-weight:600;margin-bottom:5px}
.trans-detail{font-size:13px;color:rgba(255,255,255,0.7)}
.trans-amount{font-size:18px;font-weight:bold;color:#00ff99}
.trans-time{font-size:12px;color:rgba(255,255,255,0.5);margin-top:5px}
.no-history{text-align:center;padding:30px;color:rgba(255,255,255,0.5)}
</style>
</head>
<body>
<div class="container">
<div class="header">
<a href="/menu" class="back-btn">←</a>
<h1>👤 Thông Tin Tài Khoản</h1>
</div>
<div class="info-box">
<div class="info-item"><span class="label"> User ID:</span><span class="value">{{ user_id }}</span></div>
<div class="info-item"><span class="label">👤 Tên đăng nhập:</span><span class="value">{{ username }}</span></div>
<div class="info-item"><span class="label">💰 Số dư:</span><span class="value">{{ "{:,}".format(balance) }}đ</span></div>
<div class="info-item"><span class="label">📅 Ngày tạo:</span><span class="value">{{ created_at }}</span></div>
</div>

<h2>📜 Lịch Sử Giao Dịch</h2>
<div class="history-box">
{% if transactions %}
{% for trans in transactions %}
<div class="transaction">
<div class="trans-info">
{% if trans.type == 'deposit' %}
<div class="trans-type">💳 Nạp Tiền</div>
<div class="trans-detail">Nạp tiền vào tài khoản</div>
{% elif trans.type == 'buy_key' %}
<div class="trans-type">🔑 Mua Key</div>
<div class="trans-detail">Mã: {{ trans.key_code }} | Loại: {{ trans.key_type }}</div>
{% endif %}
<div class="trans-time">🕐 {{ trans.time_str }}</div>
</div>
<div class="trans-amount">
{% if trans.type == 'deposit' %}+{% else %}-{% endif %}{{ "{:,}".format(trans.amount) }}đ
</div>
</div>
{% endfor %}
{% else %}
<div class="no-history">📭 Chưa có giao dịch nào</div>
{% endif %}
</div>
</div>
</body>
</html>"""

HTML_BUY_KEY = """<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Mua Key - SHOP MINHSANG</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Segoe UI',system-ui,-apple-system,sans-serif;background:#0a1628;color:#fff;min-height:100vh;padding:20px}
.container{max-width:1200px;margin:0 auto}
.header{display:flex;align-items:center;gap:15px;margin-bottom:30px}
.back-btn{font-size:28px;color:#00e6b4;text-decoration:none;transition:all 0.3s}
.back-btn:hover{transform:translateX(-5px)}
h1{background:linear-gradient(135deg,#00e6b4,#00b4d8);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.balance-info{text-align:center;margin-bottom:30px;padding:20px;background:rgba(13,31,54,0.9);border-radius:16px;border:1px solid rgba(0,230,180,0.2)}
.balance-info h3{color:#00e6b4;font-size:24px}
.pricing-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:30px}
.price-card{background:rgba(13,31,54,0.95);border-radius:20px;padding:30px;text-align:center;border:1px solid rgba(0,230,180,0.2);transition:all 0.3s}
.price-card:hover{transform:translateY(-8px);border-color:#00e6b4;box-shadow:0 20px 40px rgba(0,230,180,0.3)}
.duration{font-size:20px;color:#00e6b4;margin-bottom:15px;font-weight:bold}
.price{font-size:36px;color:#fff;margin-bottom:20px;font-weight:bold;background:linear-gradient(135deg,#00e6b4,#00b4d8);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.buy-btn{width:100%;padding:15px;background:linear-gradient(135deg,#00e6b4,#00b4d8);color:#0a1628;border:none;border-radius:12px;font-size:16px;font-weight:bold;cursor:pointer;margin-top:20px;transition:all 0.3s;box-shadow:0 8px 20px rgba(0,230,180,0.3)}
.buy-btn:hover{transform:scale(1.05);box-shadow:0 12px 30px rgba(0,230,180,0.5)}
.error{background:rgba(255,80,80,0.15);padding:14px;border-radius:12px;margin-bottom:20px;text-align:center;border:1px solid rgba(255,80,80,0.3);color:#ff8888}
.success{background:rgba(0,230,180,0.15);padding:14px;border-radius:12px;margin-bottom:20px;text-align:center;border:1px solid rgba(0,230,180,0.3);color:#00e6b4}
</style>
</head>
<body>
<div class="container">
<div class="header">
<a href="/menu" class="back-btn">←</a>
<h1>💎 Bảng Giá Key</h1>
</div>
{% if error %}<div class="error">{{ error }}</div>{% endif %}
{% if success %}<div class="success">{{ success|safe }}</div>{% endif %}
<div class="balance-info">
<h3>💰 Số dư hiện tại: {{ "{:,}".format(balance) }}đ</h3>
</div>
<div class="pricing-grid">
<div class="price-card">
<div class="duration">⏰ 1 Ngày</div>
<div class="price">40.000đ</div>
<form method="post" style="margin:0">
<input type="hidden" name="key_type" value="1d">
<input type="hidden" name="price" value="40000">
<button type="submit" class="buy-btn">Mua Ngay</button>
</form>
</div>
<div class="price-card">
<div class="duration">📅 1 Tuần</div>
<div class="price">120.000đ</div>
<form method="post" style="margin:0">
<input type="hidden" name="key_type" value="1t">
<input type="hidden" name="price" value="120000">
<button type="submit" class="buy-btn">Mua Ngay</button>
</form>
</div>
<div class="price-card">
<div class="duration">📆 1 Tháng</div>
<div class="price">200.000đ</div>
<form method="post" style="margin:0">
<input type="hidden" name="key_type" value="1thang">
<input type="hidden" name="price" value="200000">
<button type="submit" class="buy-btn">Mua Ngay</button>
</form>
</div>
<div class="price-card">
<div class="duration">♾️ Vĩnh Viễn</div>
<div class="price">400.000đ</div>
<form method="post" style="margin:0">
<input type="hidden" name="key_type" value="vv">
<input type="hidden" name="price" value="400000">
<button type="submit" class="buy-btn">Mua Ngay</button>
</form>
</div>
</div>
</div>
</body>
</html>"""

HTML_DEPOSIT = """<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Nạp Tiền - SHOP MINHSANG</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Segoe UI',system-ui,-apple-system,sans-serif;background:#0a1628;color:#fff;min-height:100vh;padding:20px}
.container{max-width:600px;margin:30px auto}
.header{display:flex;align-items:center;gap:15px;margin-bottom:30px}
.back-btn{font-size:28px;color:#00e6b4;text-decoration:none;transition:all 0.3s}
.back-btn:hover{transform:translateX(-5px)}
h1{background:linear-gradient(135deg,#00e6b4,#00b4d8);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.step-container{background:rgba(13,31,54,0.95);padding:30px;border-radius:20px;border:1px solid rgba(0,230,180,0.2);backdrop-filter:blur(20px);margin-bottom:20px}
.step-title{color:#00e6b4;font-size:20px;margin-bottom:20px;text-align:center}
.amount-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:15px;margin-bottom:20px}
.amount-btn{padding:15px;background:rgba(0,230,180,0.1);border:2px solid rgba(0,230,180,0.3);border-radius:12px;color:#fff;font-size:18px;font-weight:bold;cursor:pointer;transition:all 0.3s;text-align:center}
.amount-btn:hover{background:rgba(0,230,180,0.2);border-color:#00e6b4;transform:translateY(-2px)}
.amount-btn.active{background:linear-gradient(135deg,#00e6b4,#00b4d8);color:#0a1628;border-color:#00e6b4}
.custom-amount{display:flex;gap:10px;margin-top:15px}
.custom-amount input{flex:1;padding:15px;border:2px solid rgba(0,230,180,0.2);border-radius:12px;background:rgba(0,230,180,0.05);color:#fff;font-size:16px;outline:none}
.custom-amount input:focus{border-color:#00e6b4;background:rgba(0,230,180,0.1)}
.qr-container{background:rgba(13,31,54,0.95);padding:30px;border-radius:20px;text-align:center;border:1px solid rgba(0,230,180,0.2);backdrop-filter:blur(20px);display:none}
.qr-container.show{display:block}
.qr-container h3{color:#00e6b4;margin-bottom:20px}
.qr-code{background:white;padding:20px;border-radius:15px;display:inline-block;margin:20px 0;box-shadow:0 10px 30px rgba(0,230,180,0.2)}
.qr-code img{width:250px;height:250px;border-radius:10px}
.transfer-info{background:rgba(0,230,180,0.1);padding:20px;border-radius:12px;margin-top:20px;border:1px solid rgba(0,230,180,0.3)}
.transfer-info p{margin:12px 0;font-size:16px}
.transfer-info strong{color:#00e6b4}
.confirm-btn{width:100%;padding:18px;background:linear-gradient(135deg,#00e6b4,#00b4d8);border:none;border-radius:12px;font-size:18px;font-weight:bold;color:#0a1628;cursor:pointer;margin-top:20px;transition:all 0.3s;box-shadow:0 8px 20px rgba(0,230,180,0.3)}
.confirm-btn:hover{transform:translateY(-2px);box-shadow:0 12px 30px rgba(0,230,180,0.5)}
.confirm-btn:disabled{opacity:0.5;cursor:not-allowed}
.success-msg{background:rgba(0,230,180,0.15);padding:14px;border-radius:12px;margin-top:20px;text-align:center;border:1px solid rgba(0,230,180,0.3);color:#00e6b4;display:none}
.success-msg.show{display:block}
</style>
<script>
let selectedAmount = 0;
let username = "{{ username }}";

function selectAmount(amount) {
  selectedAmount = amount;
  event.target.classList.add('active');
  document.getElementById('customAmount').value = '';
  showQR();
}

function setCustomAmount() {
  const val = parseInt(document.getElementById('customAmount').value);
  if(val && val > 0) {
    selectedAmount = val;
    document.querySelectorAll('.amount-btn').forEach(btn => btn.classList.remove('active'));
    showQR();
  }
}

function showQR() {
  if(selectedAmount > 0) {
    const content = `NAP ${username} ${selectedAmount}`;
    const qrUrl = `https://img.vietqr.io/image/MB-0886027767-compact.png?amount=${selectedAmount}&addInfo=${encodeURIComponent(content)}`;
    document.getElementById('qrImage').src = qrUrl;
    document.getElementById('amountDisplay').textContent = selectedAmount.toLocaleString();
    document.getElementById('contentDisplay').textContent = content;
    document.getElementById('qrContainer').classList.add('show');
  }
}

async function confirmTransfer() {
  if(selectedAmount <= 0) return;

  const btn = document.getElementById('confirmBtn');
  btn.disabled = true;
  btn.textContent = 'Đang gửi...';

  try {
    const res = await fetch('/api/confirm-deposit', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({amount: selectedAmount})
    });
    const data = await res.json();

    if(data.ok) {
      document.getElementById('successMsg').classList.add('show');
      btn.textContent = 'Đã gửi xác nhận';
    } else {
      btn.disabled = false;
      btn.textContent = 'Xác nhận đã chuyển khoản';
      alert(data.error || 'Có lỗi xảy ra');
    }
  } catch(e) {
    btn.disabled = false;
    btn.textContent = 'Xác nhận đã chuyển khoản';
    alert('Không thể kết nối');
  }
}
</script>
</head>
<body>
<div class="container">
<div class="header">
<a href="/menu" class="back-btn">←</a>
<h1>💳 Nạp Tiền</h1>
</div>

<div class="step-container">
<div class="step-title">📊 Bước 1: Chọn số tiền muốn nạp</div>
<div class="amount-grid">
<button class="amount-btn" onclick="selectAmount(50000)">50.000đ</button>
<button class="amount-btn" onclick="selectAmount(100000)">100.000đ</button>
<button class="amount-btn" onclick="selectAmount(200000)">200.000đ</button>
<button class="amount-btn" onclick="selectAmount(500000)">500.000đ</button>
</div>
<div class="custom-amount">
<input type="number" id="customAmount" placeholder="Hoặc nhập số tiền tùy chỉnh" onchange="setCustomAmount()">
</div>
</div>

<div class="qr-container" id="qrContainer">
<h3>📱 Bước 2: Quét mã QR để chuyển khoản</h3>
<div class="qr-code">
<img id="qrImage" src="" alt="QR Code">
</div>
<div class="transfer-info">
<p><strong>Ngân hàng:</strong> MB Bank</p>
<p><strong>Số tài khoản:</strong> 0886027767</p>
<p><strong>Chủ tài khoản:</strong> TRAN MINH SANG</p>
<p><strong>Số tiền:</strong> <span id="amountDisplay">0</span>đ</p>
<p><strong>Nội dung:</strong> <span id="contentDisplay"></span></p>
</div>
<button class="confirm-btn" id="confirmBtn" onclick="confirmTransfer()">✅ Tôi đã chuyển khoản</button>
<div class="success-msg" id="successMsg">
✅ Đã nhận xác nhận! Admin sẽ kiểm tra và duyệt nạp tiền cho bạn trong giây lát.
</div>
</div>

</div>
</body>
</html>"""

HTML_ENTER_KEY = """<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Nhập Key - {{game_name}}</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Segoe UI',system-ui,-apple-system,sans-serif;background:linear-gradient(135deg,#0a1628 0%%,#0d1f36 50%%,#112a45 100%%);color:#fff;min-height:100vh;display:flex;align-items:center;justify-content:center;padding:20px;position:relative}
body::before{content:'';position:absolute;width:100%;height:100%;background:radial-gradient(circle at 30% 50%,rgba(0,230,180,0.08) 0%%,transparent 50%%);animation:pulse 6s ease-in-out infinite}
@keyframes pulse{0%%,100%%{opacity:1}50%%{opacity:0.5}}

.key-box{background:rgba(13,31,54,0.95);padding:40px;border-radius:20px;box-shadow:0 15px 40px rgba(0,0,0,0.6);width:90%;max-width:450px;border:1px solid rgba(0,230,180,0.2);backdrop-filter:blur(15px);position:relative;z-index:1}

.game-logo{text-align:center;margin-bottom:25px}
.game-logo img{width:100px;height:100px;border-radius:16px;object-fit:cover;border:2px solid rgba(0,230,180,0.3);box-shadow:0 8px 20px rgba(0,230,180,0.3)}

.game-name{text-align:center;margin-bottom:10px;font-size:16px;color:#00e6b4;font-weight:600;letter-spacing:1px;text-transform:uppercase}

.key-box h2{text-align:center;margin-bottom:30px;font-size:26px;background:linear-gradient(135deg,#00e6b4,#00b4d8);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-weight:bold;letter-spacing:0.5px}

.form-group{margin-bottom:25px}
.form-group label{display:block;margin-bottom:10px;color:#00e6b4;font-weight:600;font-size:14px}
.form-group input{width:100%;padding:16px;border:2px solid rgba(0,230,180,0.25);border-radius:12px;font-size:16px;background:rgba(0,230,180,0.08);color:#fff;outline:none;transition:all 0.3s}
.form-group input:focus{border-color:#00e6b4;background:rgba(0,230,180,0.15);box-shadow:0 0 15px rgba(0,230,180,0.2)}
.form-group input::placeholder{color:rgba(255,255,255,0.4)}

.btn{width:100%;padding:16px;background:linear-gradient(135deg,#00e6b4,#00b4d8);border:none;border-radius:12px;font-size:17px;font-weight:bold;color:#0a1628;cursor:pointer;transition:all 0.3s;box-shadow:0 6px 18px rgba(0,230,180,0.35);text-transform:uppercase;letter-spacing:0.5px}
.btn:hover{transform:translateY(-2px);box-shadow:0 10px 25px rgba(0,230,180,0.5)}
.btn:active{transform:translateY(0)}

.error{background:rgba(255,80,80,0.15);padding:14px;border-radius:12px;margin-bottom:20px;text-align:center;border:1px solid rgba(255,80,80,0.3);color:#ff8888;font-size:14px}

.info-box{margin-top:25px;padding:15px;background:rgba(255,165,0,0.1);border-radius:12px;border:1px solid rgba(255,165,0,0.3);text-align:center}
.info-box a{color:#ffb700;text-decoration:none;font-weight:600;transition:all 0.3s}
.info-box a:hover{color:#ffd700}

.back-link{text-align:center;margin-top:20px}
.back-link a{color:#00e6b4;text-decoration:none;font-size:15px;font-weight:600;transition:all 0.3s}
.back-link a:hover{color:#00b4d8}

@media(max-width:600px){
.key-box{padding:30px 20px}
.game-logo img{width:80px;height:80px}
.key-box h2{font-size:22px}
}
</style>
</head>
<body>
<div class="key-box">
<div class="game-logo">
<img src="{{game_logo}}" alt="{{game_name}}">
</div>
<div class="game-name">{{game_name}}</div>
<h2>🔑 Nhập Key Kích Hoạt</h2>
{% if error %}<div class="error">❌ {{ error }}</div>{% endif %}
<form method="post">
<div class="form-group">
<label>Mã Key:</label>
<input name="key_code" type="text" placeholder="Nhập mã key" required autofocus>
</div>
<button type="submit" class="btn">Kích hoạt</button>
</form>

<div class="info-box">
💡 Chưa có key? <a href="/buy-key">Mua ngay</a>
</div>
<div class="back-link">
<a href="/menu">← Quay lại</a>
</div>
</div>
</body>
</html>"""

HTML_GAME_LC79 = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Lc79</title>
  <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
  
  <script>
    // Hàm chuyển hướng nhanh
    function redirectToIndex() {
        // Sử dụng replace để ngăn người dùng quay lại trang tool bằng nút Back
        window.location.replace('/menu');
    }

    // Chạy hàm hiện nội dung ngay lập tức
    document.addEventListener('DOMContentLoaded', () => {
        document.body.style.display = 'block'; // Hiện body ngay sau khi DOM được tải
    });
  </script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');
    *{box-sizing:border-box;margin:0;padding:0; font-weight: 900 !important;} /* Thêm font-weight 900 cho toàn bộ trang */
    body{
      font-family:'Share Tech Mono',monospace;
      background:radial-gradient(circle at 10% 10%, rgba(0,0,0,0.6), rgba(0,0,0,1));
      color:#00ff00;height:100vh;overflow:hidden;
      display: none; /* Mặc định ẩn, sẽ được JS hiện lên ngay */
    }

    /* --- Overlays (Game Selection) --- */
    .overlay {
      position: fixed;
      inset: 0;
      background: linear-gradient(135deg, #0052D4, #4364F7, #6FB1FC);
      z-index: 100;
      display: none;
      align-items: center;
      justify-content: center;
      flex-direction: column;
      gap: 20px;
      transition: opacity 0.3s ease;
    }

    /* iframe behind UI */
    #fullscreenIframe{position:fixed;inset:0;width:100%;height:100%;border:0;z-index:1;}

    /* Main content initially hidden */
    .panel, #predictionPopup, .footer-text { display: flex; }

    /* Left panel */
    .panel{
      position:fixed;left:12px;top:12px;z-index:55;
      display:flex;flex-direction:column;gap:8px;
      width:178px; /* ĐÃ SỬA: Giảm 2px từ 180px xuống 178px */
      font-weight: 900; /* In đậm panel */
    }
    .btn{
      background:rgba(0,255,0,0.09);
      color:#00ff00;border:1px solid rgba(0,255,0,0.25);
      padding:6px 8px; /* Giảm padding để nút nhỏ lại */
      border-radius:8px;font-size:13px;text-align:center;
      cursor:pointer;transition:0.12s;
      font-weight: 900; /* In đậm chữ trên nút */
    }
    .btn:hover{transform:translateY(-2px)}
    .btn:disabled{cursor:not-allowed;opacity:0.6;transform:none; font-weight: 900 !important;}
    .logout-btn{
      background:linear-gradient(90deg,#2b0000,#700000);color:#fff;border:1px solid #ff3b3b;
      font-weight: 900; /* In đậm chữ trên nút */
    }

    /* === Khung nháy và hiệu ứng MỚI của bạn (Đã thêm chút đỏ cho nền) === */
    .prediction-box {
      position: fixed;
      bottom: 120px; 
      left: 50%;
      transform: translateX(-50%);
      /* ĐÃ SỬA: Thêm màu đỏ nổi bật hơn theo yêu cầu */
      background: linear-gradient(to bottom, #ffeb3b, #ff0000, #ff0000); /* Vàng -> Đỏ (Đỏ chiếm ưu thế hơn) */
      border-radius: 20px;
      border: 2px solid #fff;
      padding: 8px 20px; 
      display: none;
      align-items: flex-end;
      justify-content: center;
      gap: 15px; 
      box-shadow: 0 4px 12px rgba(0,0,0,0.4);
      z-index: 99999;
      cursor: move;
      touch-action: none;
      font-weight: 900; /* In đậm khung dự đoán */
    }
    
    .prediction-box .item {
        display:flex;
        flex-direction:column;
        align-items:center;
    }
    
    .prediction-box .label {
        font-weight:900; 
        font-size:18px; 
        margin-bottom:6px; 
        color:#000;
    }
    
    .prediction-box .circle {
        width:40px; 
        height:40px; 
        border-radius:50%; 
        border:3px solid #fff; 
        display:flex; 
        align-items:center; 
        justify-content:center; 
        font-weight:900; /* In đậm số trong vòng tròn */
        font-size:18px; 
        opacity:0.2;
        transition: opacity 0.3s, box-shadow 0.3s, background 0.3s;
    }
    
    /* Màu nháy mới cho TÀI (Giữ nguyên Xanh Lá) */
    .circle.active.tai {
      background: #00ff00;
      opacity:1; 
      box-shadow:0 0 10px #00ff00, 0 0 20px #00ff00;
    }

    /* Màu nháy mới cho XỈU (Màu Đỏ) */
    .circle.active.xiu {
      background: #ff0000; /* Màu đỏ */
      opacity:1; 
      box-shadow:0 0 10px #ff0000, 0 0 20px #ff0000;
    }
    
    .prediction-box .logo {
        width:55px; 
        height:auto;
        margin-bottom: 2px;
    }
    
    .prediction-box .close-btn {
        position:absolute;
        top:0px;
        right:4px;
        cursor:pointer;
        font-size:18px;
        font-weight:900; /* In đậm nút đóng */
        color:#000;
    }
    
    /* CSS Cập nhật cho thông tin Phiên/Dự đoán/Độ tin cậy */
    .footer-text{
        position:fixed;
        bottom:8px;
        right:12px; /* Căn phải */
        font-size:13px;
        color:#00ff00;
        text-shadow:0 0 5px #00ff00,0 0 10px #00ff00;
        z-index:50;
        display:flex; /* Hiển thị ngang hàng */
        align-items: center; 
        justify-content: flex-end;
        line-height: 1.4;
        padding: 5px 8px; 
        background: rgba(0, 0, 0, 0.3); 
        border-radius: 5px;
        white-space: nowrap; /* Đảm bảo không xuống dòng */
        font-weight: 900; /* In đậm footer */
    }

    /* Keyframe ĐÃ SỬA để nhấp nháy mượt mà hơn (dùng ease-in-out thay vì step-end) */
    @keyframes textBlinkSmooth {
      0% { opacity: 1; }
      50% { opacity: 0.5; }
      100% { opacity: 1; }
    }
    
    /* Áp dụng hiệu ứng nhấp nháy chữ mượt mà */
    .blinking-text {
      animation: textBlinkSmooth 1s ease-in-out infinite; /* Thay step-end bằng ease-in-out */
    }

    @media(max-width:480px){
      #predictionPopup{width:200px; height: 90px; right:8px;top:60px} 
      .prediction-circle { width: 40px; height: 40px; }
      .dice-icon { font-size: 24px; }
    }
  </style>
</head>
<body>
  <iframe id="fullscreenIframe" src="https://lc79a.bet" name="fullscreenIframe"></iframe>
  <div class="panel">
    <button id="activateBtn" class="btn">Kích Hoạt</button>
    <button id="logoutBtn" class="btn logout-btn">Quay Về</button>
  </div>
  
  <div id="predictionPopup" class="prediction-box" role="dialog" aria-hidden="true">
    <div class="item">
        <span class="label">TÀI</span>
        <div id="taiCircle" class="circle tai"></div>
    </div>
    <img src="https://i.postimg.cc/Xvwzw7fT/3E497BE2-D59F-46D3-BCCF-FDC2E3A9929C.png" alt="Logo" class="logo">
    <div class="item">
        <span class="label">XỈU</span>
        <div id="xiuCircle" class="circle xiu"></div>
    </div>
    <span class="close-btn">✖</span>
  </div>

  <div class="footer-text">
    <div id="footerInfo" class="blinking-text">
      Phiên: --- | Dự Đoán: --- | Độ Tin Cậy: ---
    </div>
  </div>
  <script>
  /* --- Element References --- */
  const fullscreenIframe = document.getElementById('fullscreenIframe');

  const activateBtn = document.getElementById('activateBtn');
  const logoutBtn = document.getElementById('logoutBtn');
  const predictionPopup = document.getElementById('predictionPopup');
  const footerInfo = document.getElementById('footerInfo');
  
  const taiCircle = document.getElementById('taiCircle');
  const xiuCircle = document.getElementById('xiuCircle');
  const closePopup = predictionPopup.querySelector('.close-btn');

  /* --- State & Config --- */
  let fetchIntervalId = null;
  let blinkIntervalId = null; 
  let currentSessionId = null; // Biến lưu trữ phiên hiện tại từ API
  let isAwaitingNewSession = false; // Biến cờ để ngăn fetchPrediction() gọi startPredictionBlink() trong thời gian chờ 6 giây
  const API_URL = 'https://apilc79-predictor.onrender.com/api/taixiumd5/lc79';

  /* --- Logout Logic (ĐÃ SỬA: Chuyển về dashboardtool.html) --- */
  logoutBtn.addEventListener('click', () => {
    window.location.href = '/menu'; // SỬA ĐỔI NÀY
  });

  /* --- API & Prediction Logic --- */

  // Hàm định dạng kết quả (viết hoa chữ cái đầu)
  function capitalize(s) {
    if (!s) return '---';
    // Đảm bảo chữ cái đầu được viết hoa, phần còn lại viết thường
    return s.charAt(0).toUpperCase() + s.slice(1).toLowerCase();
  }

  async function fetchPrediction() {
    try {
      const response = await fetch(API_URL);
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      console.log("Dữ liệu API:", data);

      const rawPrediction = data.du_doan;
      const predictedResult = rawPrediction.toLowerCase() === 'tài' ? 'T' : 'X';
      const nextSessionId = data.phien_hien_tai;
      const confidence = data.do_tin_cay;
      
      // Định dạng lại kết quả (Phiên, Dự đoán, Độ tin cậy)
      const formattedPrediction = capitalize(rawPrediction);
      const formattedConfidence = confidence ? `${confidence}%` : '---';

      // Cập nhật thông tin ở góc phải dưới cùng
      footerInfo.textContent = `Phiên: ${nextSessionId} | Dự Đoán: ${formattedPrediction} | Độ Tin Cậy: ${formattedConfidence}`;

      // Nếu đang trong thời gian chờ 6 giây, không làm gì cả
      if (isAwaitingNewSession) {
          console.log(`Đang chờ hết 6 giây cho phiên ${currentSessionId}. Bỏ qua nháy.`);
          return;
      }
      
      // Xử lý logic nháy
      if (currentSessionId && currentSessionId !== nextSessionId) {
        // Hết phiên (Phiên đã thay đổi: 1 -> 2)
        console.log(`Phiên thay đổi: ${currentSessionId} -> ${nextSessionId}. Bắt đầu ngưng nháy 6 giây.`);
        stopBlink(); // Dừng nháy cũ ngay lập tức
        isAwaitingNewSession = true; // Bật cờ chờ
        currentSessionId = nextSessionId; // Cập nhật phiên mới

        // Bắt đầu nháy sau 6 giây (Đúng nhịp yêu cầu)
        setTimeout(() => {
          isAwaitingNewSession = false; // Tắt cờ chờ
          console.log(`Hết 6 giây. Bắt đầu nháy cho phiên mới: ${currentSessionId}`);
          // Gọi lại startPredictionBlink với dữ liệu dự đoán mới nhất
          startPredictionBlink(predictedResult); 
        }, 6000); 
      } else if (currentSessionId === null || currentSessionId === nextSessionId) {
          // Lần đầu chạy HOẶC vẫn trong cùng phiên, Bắt đầu/Tiếp tục nháy
          currentSessionId = nextSessionId; // Đảm bảo phiên đã được đặt
          if (!blinkIntervalId) {
             startPredictionBlink(predictedResult);
          }
      } 

    } catch (error) {
      console.error("Lỗi khi fetch API:", error);
      footerInfo.textContent = 'Lỗi kết nối API!';
      stopBlink();
    }
  }

  function startPredictionBlink(predictedResult) {
      // Đảm bảo dừng nháy cũ trước khi bắt đầu cái mới
      stopBlink(); 
      
      const targetCircle = (predictedResult === 'T') ? taiCircle : xiuCircle;
      const otherCircle = (predictedResult === 'T') ? xiuCircle : taiCircle;

      // Đảm bảo nút còn lại bị tắt
      otherCircle.classList.remove("active"); 

      // Bắt đầu nháy
      let isBlinking = true;
      blinkIntervalId = setInterval(()=>{
          if(isBlinking){
              targetCircle.classList.add("active");
          } else {
              targetCircle.classList.remove("active");
          }
          isBlinking = !isBlinking;
      }, 500); // Nháy mỗi 0.5 giây
  }

  function stopBlink(){
      if(blinkIntervalId){
          clearInterval(blinkIntervalId);
          blinkIntervalId = null;
          taiCircle.classList.remove("active");
          xiuCircle.classList.remove("active");
      }
  }

  activateBtn.addEventListener('click', () => {
    if (activateBtn.disabled) return; 

    predictionPopup.style.display = 'flex';
    activateBtn.disabled = true;
    activateBtn.textContent = 'Đang Chạy';

    // Reset trạng thái khi kích hoạt
    currentSessionId = null; 
    isAwaitingNewSession = false;
    stopBlink(); // Dừng nháy cũ (nếu có)

    // Lấy dự đoán ngay lập tức
    fetchPrediction(); 
    // Thiết lập chu kỳ lấy dự đoán mỗi 1 giây (để theo dõi nhịp phiên nhanh và chính xác)
    fetchIntervalId = setInterval(fetchPrediction, 1000); 
  });

  closePopup.addEventListener('click', () => {
    predictionPopup.style.display = 'none';
    if (fetchIntervalId) {
      clearInterval(fetchIntervalId);
      fetchIntervalId = null;
      activateBtn.disabled = false;
      activateBtn.textContent = 'Kích Hoạt';
      stopBlink(); 
      footerInfo.textContent = 'Phiên: --- | Dự Đoán: --- | Độ Tin Cậy: ---'; // Reset info
    }
  });

  /* === Logic Kéo thả (Giữ nguyên và hoạt động mượt mà) === */
  (function makeDraggable(el){
    let startX = 0, startY = 0;
    
    const dragStart = (e) => {
        if (e.target.classList.contains("close-btn")) return;
        e.preventDefault();
        
        // Cải tiến: Tính toán vị trí ban đầu của phần tử để kéo mượt hơn
        const rect = el.getBoundingClientRect();
        
        // Lấy tọa độ con trỏ/ngón tay
        let clientX = e.type.includes("touch") ? e.touches[0].clientX : e.clientX;
        let clientY = e.type.includes("touch") ? e.touches[0].clientY : e.clientY;
        
        // Lưu trữ điểm offset (khoảng cách từ góc trên-trái của phần tử đến con trỏ)
        startX = clientX - rect.left;
        startY = clientY - rect.top;
        
        // Đặt vị trí tuyệt đối ban đầu nếu chưa có
        if (el.style.position !== 'fixed' || el.style.transform !== "none") {
             el.style.left = rect.left + 'px';
             el.style.top = rect.top + 'px';
             el.style.position = 'fixed';
             el.style.right = "auto";
             el.style.bottom = "auto";
             el.style.transform = "none"; 
        }

        document.addEventListener("mousemove", dragging);
        document.addEventListener("mouseup", dragEnd);
        document.addEventListener("touchmove", dragging, { passive: false });
        document.addEventListener("touchend", dragEnd);
    };

    const dragging = (e) => {
        let clientX = e.type.includes("touch") ? e.touches[0].clientX : e.clientX;
        let clientY = e.type.includes("touch") ? e.touches[0].clientY : e.clientY;
        
        // Tính toán vị trí mới
        let newX = clientX - startX;
        let newY = clientY - startY;

        // Giới hạn trong khung nhìn (tuỳ chọn)
        const maxX = window.innerWidth - el.offsetWidth;
        const maxY = window.innerHeight - el.offsetHeight;
        
        newX = Math.max(0, Math.min(newX, maxX));
        newY = Math.max(0, Math.min(newY, maxY));
        
        el.style.left = newX + "px";
        el.style.top = newY + "px";
        e.preventDefault();
    };

    const dragEnd = () => {
        document.removeEventListener("mousemove", dragging);
        document.removeEventListener("mouseup", dragEnd);
        document.removeEventListener("touchmove", dragging);
        document.removeEventListener("touchend", dragEnd);
    };

    el.addEventListener("mousedown", dragStart);
    el.addEventListener("touchstart", dragStart);
  })(predictionPopup);
  </script>
</body>
</html>"""

HTML_GAME_LUCK8 = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Luck8</title>
  <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
  
  <script>
    // Hàm chuyển hướng nhanh
    function redirectToIndex() {
        window.location.replace('/menu');
    }

    // Chạy hàm hiện nội dung ngay lập tức
    document.addEventListener('DOMContentLoaded', () => {
        document.body.style.display = 'block'; 
    });
  </script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');
    *{box-sizing:border-box;margin:0;padding:0}
    body{
      font-family:'Share Tech Mono',monospace;
      background:radial-gradient(circle at 10% 10%, rgba(0,0,0,0.6), rgba(0,0,0,1));
      color:#00ff00;height:100vh;overflow:hidden;
      display: none; 
    }

    .btn, .footer-text, .prediction-box .label, .prediction-box .circle, .prediction-box .close-btn {
        font-weight: 700 !important;
    }
    
    .overlay {
      position: fixed;
      inset: 0;
      background: linear-gradient(135deg, #0052D4, #4364F7, #6FB1FC);
      z-index: 100;
      display: none;
      align-items: center;
      justify-content: center;
      flex-direction: column;
      gap: 20px;
      transition: opacity 0.3s ease;
    }

    #fullscreenIframe{position:fixed;inset:0;width:100%;height:100%;border:0;z-index:1;}

    .panel, #predictionPopup, .footer-text { display: flex; }

    .panel{
      position:fixed;left:12px;top:12px;z-index:55;
      display:flex;flex-direction:column;gap:8px;width:180px;
    }
    .btn{
      background:rgba(0,255,0,0.09);
      color:#00ff00;border:1px solid rgba(0,255,0,0.25);
      padding:6px 8px; 
      border-radius:8px;font-size:13px;text-align:center;
      cursor:pointer;transition:0.12s;
    }
    .btn:hover{transform:translateY(-2px)}
    .btn:disabled{cursor:not-allowed;opacity:0.6;transform:none;}
    .logout-btn{
      background:linear-gradient(90deg,#2b0000,#700000);color:#fff;border:1px solid #ff3b3b;
    }

    .prediction-box {
      position: fixed;
      bottom: 120px; 
      left: 50%;
      transform: translateX(-50%);
      background: linear-gradient(90deg, #005600, #00008B); 
      border-radius: 18px; 
      border: 1px solid #ffcc00; 
      padding: 6px 18px; 
      display: none;
      align-items: flex-end;
      justify-content: center;
      gap: 13px; 
      box-shadow: 0 0 15px 5px rgba(255, 204, 0, 0.3); 
      z-index: 99999;
      cursor: move;
      touch-action: none;
    }
    
    .prediction-box .item {
        display:flex;
        flex-direction:column;
        align-items:center;
    }
    
    .prediction-box .label {
        font-weight:700; 
        font-size:17px; 
        margin-bottom:5px; 
        color:#000000; 
    }
    
    .prediction-box .circle {
        width:38px; 
        height:38px; 
        border-radius:50%; 
        border:3px solid #ffcc00; 
        display:flex; 
        align-items:center; 
        justify-content:center; 
        font-weight:700; 
        font-size:17px; 
        opacity:0.2;
        transition: opacity 0.3s, box-shadow 0.3s, background 0.3s;
        color: #000; 
    }
    
    .circle.active.tai {
      background: #00ff00;
      opacity:1; 
      box-shadow:0 0 10px #00ff00, 0 0 20px #00ff00;
    }

    .circle.active.xiu {
      background: #ff0000; 
      opacity:1; 
      box-shadow:0 0 10px #ff0000, 0 0 20px #ff0000;
    }
    
    .prediction-box .logo {
        width:53px; 
        height:auto;
        margin-bottom: 2px;
    }
    
    .prediction-box .close-btn {
        position:absolute;
        top:0px;
        right:4px;
        cursor:pointer;
        font-size:17px; 
        font-weight:700; 
        color:#000000; 
    }
    
    .footer-text{
        position:fixed;
        bottom:8px;
        right:12px; 
        font-size:13px;
        color:#00ff00;
        text-shadow:0 0 5px #00ff00,0 0 10px #00ff00;
        z-index:50;
        display:flex; 
        align-items: center; 
        justify-content: flex-end;
        line-height: 1.4;
        padding: 5px 8px; 
        background: rgba(0, 0, 0, 0.3); 
        border-radius: 5px;
        white-space: nowrap; 
        font-weight: 700; 
    }

    @keyframes textBlinkSmooth {
      0% { opacity: 1; }
      50% { opacity: 0.5; }
      100% { opacity: 1; }
    }
    
    .blinking-text {
      animation: textBlinkSmooth 1s ease-in-out infinite; 
    }

    @media(max-width:480px){
      #predictionPopup{width:190px; height: 85px; right:8px;top:60px} 
      .prediction-box { padding: 5px 15px; } 
      .prediction-box .circle { width: 36px; height: 36px; } 
    }
  </style>
</head>
<body>
  <iframe id="fullscreenIframe" src="https://japb3yw.bbb5lol.cc/mobile/?inviteCode=4592386#/" name="fullscreenIframe"></iframe>
  <div class="panel">
    <button id="activateBtn" class="btn">Kích Hoạt</button>
    <button id="logoutBtn" class="btn logout-btn">Quay Về</button>
  </div>
  
  <div id="predictionPopup" class="prediction-box" role="dialog" aria-hidden="true">
    <div class="item">
        <span class="label">TÀI</span>
        <div id="taiCircle" class="circle tai"></div>
    </div>
    <img src="https://i.postimg.cc/D0Yj2Wht/IMG-7951.png" alt="Logo" class="logo">
    <div class="item">
        <span class="label">XỈU</span>
        <div id="xiuCircle" class="circle xiu"></div>
    </div>
    <span class="close-btn">✖</span>
  </div>

  <div class="footer-text">
    <div id="footerInfo" class="blinking-text">
      Phiên: --- | Dự Đoán: --- | Độ Tin Cậy: ---
    </div>
  </div>
  <script>
  const fullscreenIframe = document.getElementById('fullscreenIframe');
  const activateBtn = document.getElementById('activateBtn');
  const logoutBtn = document.getElementById('logoutBtn');
  const predictionPopup = document.getElementById('predictionPopup');
  const footerInfo = document.getElementById('footerInfo');
  const taiCircle = document.getElementById('taiCircle');
  const xiuCircle = document.getElementById('xiuCircle');
  const closePopup = predictionPopup.querySelector('.close-btn');

  let fetchIntervalId = null;
  let blinkIntervalId = null; 
  let currentSessionId = null; 
  let isAwaitingNewSession = false; 
  const API_URL = '/api/predict/luck8';

  logoutBtn.addEventListener('click', () => {
    window.location.href = '/menu';
  });

  function capitalize(s) {
    if (!s) return '---';
    return s.charAt(0).toUpperCase() + s.slice(1).toLowerCase();
  }

  async function fetchPrediction() {
    try {
      const response = await fetch(API_URL);
      if (!response.ok) throw new Error('Network response was not ok');
      const json = await response.json();
      if (!json.ok) throw new Error(json.error || 'API Error');
      const data = json.result;
      console.log("Dữ liệu API:", data);

      const rawPrediction = data.du_doan;
      const predictedResult = rawPrediction && rawPrediction.toLowerCase() === 'tài' ? 'T' : 'X';
      const nextSessionId = data.phien ? parseInt(data.phien) + 1 : '---';
      let confidence = data.do_tin_cay;
      if (confidence && confidence <= 1) confidence = Math.round(confidence * 100);
      
      const formattedPrediction = capitalize(rawPrediction);
      const formattedConfidence = confidence ? `${confidence}%` : '---';

      footerInfo.textContent = `Phiên: ${nextSessionId} | Dự Đoán: ${formattedPrediction} | Độ Tin Cậy: ${formattedConfidence}`;

      if (isAwaitingNewSession) {
          console.log(`Đang chờ hết 6 giây cho phiên ${currentSessionId}. Bỏ qua nháy.`);
          return;
      }
      
      if (currentSessionId && currentSessionId !== nextSessionId) {
        console.log(`Phiên thay đổi: ${currentSessionId} -> ${nextSessionId}. Bắt đầu ngưng nháy 6 giây.`);
        stopBlink(); 
        isAwaitingNewSession = true; 
        currentSessionId = nextSessionId; 

        setTimeout(() => {
          isAwaitingNewSession = false; 
          console.log(`Hết 6 giây. Bắt đầu nháy cho phiên mới: ${currentSessionId}`);
          startPredictionBlink(predictedResult); 
        }, 6000); 
      } else if (currentSessionId === null || currentSessionId === nextSessionId) {
          currentSessionId = nextSessionId; 
          if (!blinkIntervalId) {
             startPredictionBlink(predictedResult);
          }
      } 

    } catch (error) {
      console.error("Lỗi khi fetch API:", error);
      footerInfo.textContent = 'Lỗi kết nối API!';
      stopBlink();
    }
  }

  function startPredictionBlink(predictedResult) {
      stopBlink(); 
      const targetCircle = (predictedResult === 'T') ? taiCircle : xiuCircle;
      const otherCircle = (predictedResult === 'T') ? xiuCircle : taiCircle;
      otherCircle.classList.remove("active"); 
      let isBlinking = true;
      blinkIntervalId = setInterval(()=>{
          if(isBlinking){
              targetCircle.classList.add("active");
          } else {
              targetCircle.classList.remove("active");
          }
          isBlinking = !isBlinking;
      }, 500); 
  }

  function stopBlink(){
      if(blinkIntervalId){
          clearInterval(blinkIntervalId);
          blinkIntervalId = null;
          taiCircle.classList.remove("active");
          xiuCircle.classList.remove("active");
      }
  }

  activateBtn.addEventListener('click', () => {
    if (activateBtn.disabled) return; 
    predictionPopup.style.display = 'flex';
    activateBtn.disabled = true;
    activateBtn.textContent = 'Đang Chạy';
    activateBtn.style.fontWeight = '700'; 
    currentSessionId = null; 
    isAwaitingNewSession = false;
    stopBlink(); 
    fetchPrediction(); 
    fetchIntervalId = setInterval(fetchPrediction, 1000); 
  });

  closePopup.addEventListener('click', () => {
    predictionPopup.style.display = 'none';
    if (fetchIntervalId) {
      clearInterval(fetchIntervalId);
      fetchIntervalId = null;
      activateBtn.disabled = false;
      activateBtn.textContent = 'Kích Hoạt';
      activateBtn.style.fontWeight = '700'; 
      stopBlink(); 
      footerInfo.textContent = 'Phiên: --- | Dự Đoán: --- | Độ Tin Cậy: ---'; 
    }
  });

  (function makeDraggable(el){
    let startX = 0, startY = 0;
    const dragStart = (e) => {
        if (e.target.classList.contains("close-btn")) return;
        e.preventDefault();
        const rect = el.getBoundingClientRect();
        let clientX = e.type.includes("touch") ? e.touches[0].clientX : e.clientX;
        let clientY = e.type.includes("touch") ? e.touches[0].clientY : e.clientY;
        startX = clientX - rect.left;
        startY = clientY - rect.top;
        if (el.style.position !== 'fixed' || el.style.transform !== "none") {
             el.style.left = rect.left + 'px';
             el.style.top = rect.top + 'px';
             el.style.position = 'fixed';
             el.style.right = "auto";
             el.style.bottom = "auto";
             el.style.transform = "none"; 
        }
        document.addEventListener("mousemove", dragging);
        document.addEventListener("mouseup", dragEnd);
        document.addEventListener("touchmove", dragging, { passive: false });
        document.addEventListener("touchend", dragEnd);
    };
    const dragging = (e) => {
        let clientX = e.type.includes("touch") ? e.touches[0].clientX : e.clientX;
        let clientY = e.type.includes("touch") ? e.touches[0].clientY : e.clientY;
        let newX = clientX - startX;
        let newY = clientY - startY;
        const maxX = window.innerWidth - el.offsetWidth;
        const maxY = window.innerHeight - el.offsetHeight;
        newX = Math.max(0, Math.min(newX, maxX));
        newY = Math.max(0, Math.min(newY, maxY));
        el.style.left = newX + "px";
        el.style.top = newY + "px";
        e.preventDefault();
    };
    const dragEnd = () => {
        document.removeEventListener("mousemove", dragging);
        document.removeEventListener("mouseup", dragEnd);
        document.removeEventListener("touchmove", dragging);
        document.removeEventListener("touchend", dragEnd);
    };
    el.addEventListener("mousedown", dragStart);
    el.addEventListener("touchstart", dragStart);
  })(predictionPopup);
  </script>
</body>
</html>"""

HTML_GAME = """<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{game}} - SHOP MINHSANG</title>
<script src="https://cdn.jsdelivr.net/npm/particles.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif;background:url('https://i.postimg.cc/hPHzbKdb/HD-wallpaper-saturn-2-blue-galaxy-planet-ring-sky-space-stars-universe.jpg') no-repeat center center;background-size:cover;color:#fff;min-height:100vh;overflow:hidden;position:relative}
body::before{content:'';position:absolute;top:0;left:0;width:100%;height:100%;background:radial-gradient(circle at center,rgba(0,40,80,0.3) 0%,rgba(0,0,30,0.7) 100%);z-index:0}
#particles-js{position:fixed;width:100%;height:100%;z-index:1;pointer-events:none}
.header{background:rgba(13,31,54,0.95);padding:18px 25px;display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid rgba(0,230,180,0.2);backdrop-filter:blur(20px);position:relative;z-index:10}
.game-title{font-size:24px;font-weight:bold;background:linear-gradient(135deg,#00e6b4,#00b4d8);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.back-btn{padding:12px 28px;background:linear-gradient(135deg,#00e6b4,#00b4d8);color:#0a1628;text-decoration:none;border-radius:12px;font-weight:bold;transition:all 0.3s;box-shadow:0 5px 15px rgba(0,230,180,0.3)}
.back-btn:hover{transform:translateY(-2px);box-shadow:0 8px 20px rgba(0,230,180,0.5)}

.iframe-container{position:absolute;top:70px;left:0;right:0;bottom:0;display:none;z-index:5}
.iframe-container iframe{width:100%;height:100%;border:none}

.robot-flash{animation:robotFlash 0.8s ease-in-out 3}
@keyframes robotFlash{
0%{filter:brightness(1) drop-shadow(0 0 0 transparent);transform:scale(1)}
50%{filter:brightness(1.3) drop-shadow(0 0 15px #00e6b4);transform:scale(1.05)}
100%{filter:brightness(1) drop-shadow(0 0 0 transparent);transform:scale(1)}
}
.widget{position:absolute;top:30px;left:30px;background:linear-gradient(145deg,#ffd66b,#d4a136);border-radius:24px;padding:25px 32px;display:none;flex-direction:column;align-items:center;font-weight:bold;width:360px;box-shadow:0 15px 35px rgba(0,0,0,0.9),inset 0 4px 12px rgba(255,255,255,0.4),0 0 50px rgba(255,215,0,0.3);border:4px solid rgba(255,215,0,0.6);cursor:move;z-index:9999;backdrop-filter:blur(10px);transition:all 0.4s ease}
.widget .session{font-size:22px;margin-bottom:16px;color:#fff;text-shadow:0 0 10px #ff0,0 0 20px #f90,0 0 30px #f60;letter-spacing:1.5px;animation:glowText 1.5s ease-in-out infinite alternate;font-weight:800}
@keyframes glowText{from{text-shadow:0 0 8px #fff,0 0 15px #f9d423,0 0 25px #ffb347}to{text-shadow:0 0 12px #ffe97a,0 0 25px #ffcc00,0 0 35px #ff9100}}
.widget .row{display:flex;justify-content:center;align-items:center;width:100%;gap:5px}
.widget .side{display:flex;flex-direction:column;align-items:center;flex:1;font-size:19px;color:#fff;text-shadow:0 0 10px #000,0 0 18px #222;font-weight:700}
.widget .dot{width:60px;height:60px;border-radius:50%;background:#1a1a1a;box-shadow:inset 0 0 20px rgba(0,0,0,0.9),0 4px 8px rgba(0,0,0,0.5);border:4px solid rgba(255,255,255,0.25);transition:all 0.5s ease;margin-bottom:8px}
.widget .on-green{background:radial-gradient(circle at 35% 35%,#c0ffc0,#00dd00,#008800);box-shadow:0 0 25px #7CFF7C,0 0 45px #00ff00,inset 0 0 20px #005500,0 8px 15px rgba(0,255,0,0.4)}
.widget .on-red{background:radial-gradient(circle at 35% 35%,#ffc0c0,#dd0000,#880000);box-shadow:0 0 25px #FF7C7C,0 0 45px #ff0000,inset 0 0 20px #550000,0 8px 15px rgba(255,0,0,0.4)}
@keyframes blink{0%%,100%%{opacity:1;transform:scale(1);filter:brightness(1.2)}50%%{opacity:0.7;transform:scale(1.15);filter:brightness(1.5)}}
.widget .blink{animation:blink 0.8s ease-in-out infinite}
.widget .center-logo{margin:-30px 22px 0 22px;transform:scale(1);transition:transform 0.3s}
.widget .center-logo img{height:70px;border-radius:16px;box-shadow:0 0 20px rgba(0,0,0,0.9),0 0 25px gold,0 4px 12px rgba(255,215,0,0.5);animation:pulseLogo 2s ease-in-out infinite;border:3px solid rgba(255,215,0,0.6)}
@keyframes pulseLogo{0%,100%{transform:scale(1);box-shadow:0 0 20px rgba(0,0,0,0.9),0 0 25px gold}50%{transform:scale(1.08);box-shadow:0 0 30px rgba(0,0,0,0.9),0 0 40px gold,0 0 50px #ffd700}}
.widget.shake{animation:shakeAnim 0.5s}
@keyframes shakeAnim{0%{transform:translate(0,0) rotate(0deg)}10%{transform:translate(-3px,-3px) rotate(-2deg)}20%{transform:translate(3px,-2px) rotate(2deg)}30%{transform:translate(-2px,3px) rotate(-1deg)}40%{transform:translate(2px,2px) rotate(1deg)}50%{transform:translate(-3px,1px) rotate(-2deg)}60%{transform:translate(3px,-3px) rotate(2deg)}70%{transform:translate(-2px,-1px) rotate(-1deg)}80%{transform:translate(2px,3px) rotate(1deg)}90%{transform:translate(-3px,-2px) rotate(-2deg)}100%{transform:translate(0,0) rotate(0deg)}}

.wrapper{max-width:360px;margin:20px auto;background:rgba(0,20,40,0.9);padding:20px;border-radius:16px;box-shadow:0 0 25px rgba(0,200,255,0.4);backdrop-filter:blur(10px);border:1px solid rgba(0,200,255,0.3);position:relative;overflow:hidden;z-index:10;display:none}
.wrapper::before{content:'';position:absolute;top:-50%;left:-50%;width:200%;height:200%;background:linear-gradient(to bottom right,transparent 0%,rgba(0,255,255,0.05) 50%,transparent 100%);transform:rotate(30deg);animation:shine 6s infinite linear}
@keyframes shine{0%{transform:rotate(30deg) translate(-30%,-30%)}100%{transform:rotate(30deg) translate(30%,30%)}}
.game-title-main{text-align:center;color:#00ffff;text-shadow:0 0 10px #00ffff;margin-bottom:15px;font-size:22px;letter-spacing:1px;position:relative}
.game-title-main::after{content:'';display:block;width:100px;height:2px;background:linear-gradient(90deg,transparent,#00ffff,transparent);margin:10px auto;border-radius:2px}
.prediction-box{display:flex;justify-content:space-around;align-items:center;margin:15px 0}
.prediction-item{text-align:center;flex:1}
.prediction-item .label{font-size:14px;color:#66ccff;margin-bottom:10px;text-transform:uppercase;letter-spacing:1px}
.prediction-item .value{font-size:24px;font-weight:bold;padding:10px 15px;border-radius:10px;background:rgba(0,10,20,0.7);border:1px solid rgba(0,255,255,0.3);box-shadow:0 0 15px rgba(0,200,255,0.2);min-width:90px;display:inline-block}
.status-info{background:rgba(0,60,120,0.3);border-radius:10px;padding:12px;margin:15px 0;border:1px solid rgba(0,200,255,0.2)}
.status-row{display:flex;justify-content:space-between;align-items:center;padding:6px 0;color:#fff;font-size:13px}
.status-row .stat-label{color:#00ccff}
.status-row .stat-value{font-weight:bold;color:#00ff99}
@keyframes float{0%%,100%%{transform:translateY(0)}50%%{transform:translateY(-8px)}}
.float-1{animation:float 3s ease-in-out infinite}
.float-2{animation:float 3s ease-in-out infinite 0.3s}
.float-3{animation:float 3s ease-in-out infinite 0.6s}
.float-4{animation:float 3s ease-in-out infinite 0.9s}
@keyframes pulse{0%%,100%%{transform:scale(1)}50%%{transform:scale(1.05)}}
.prediction-value{animation:pulse 2s ease-in-out infinite}

.luck8-container{position:fixed;top:50%;left:50%;transform:translate(-50%,-50%);width:95%;max-width:420px;background:linear-gradient(145deg,rgba(10,25,47,0.98),rgba(15,35,60,0.98));backdrop-filter:blur(25px);border-radius:25px;padding:25px;border:2px solid rgba(79,195,247,0.3);box-shadow:0 20px 50px rgba(0,0,0,0.6),0 0 80px rgba(79,195,247,0.15);z-index:10;display:none}
.luck8-session{text-align:center;font-size:20px;color:#4fc3f7;margin-bottom:25px;font-weight:600;padding:12px 20px;background:rgba(79,195,247,0.1);border-radius:12px;border:1px solid rgba(79,195,247,0.3)}
.luck8-session span{color:#81d4fa;font-weight:bold;font-size:22px}
.luck8-circle-container{display:flex;justify-content:center;gap:30px;margin-bottom:25px}
.luck8-circle{width:110px;height:110px;border-radius:50%;display:flex;flex-direction:column;justify-content:center;align-items:center;background:rgba(20,40,70,0.8);border:3px solid rgba(255,255,255,0.2);transition:all 0.4s;box-shadow:0 8px 20px rgba(0,0,0,0.4)}
.luck8-tai{border-color:#00ff88;background:linear-gradient(145deg,rgba(0,255,136,0.2),rgba(0,255,136,0.05))}
.luck8-xiu{border-color:#ff4444;background:linear-gradient(145deg,rgba(255,68,68,0.2),rgba(255,68,68,0.05))}
.luck8-icon{font-size:42px;margin-bottom:8px;filter:drop-shadow(0 0 10px currentColor)}
.luck8-tai .luck8-icon{color:#00ff88}
.luck8-xiu .luck8-icon{color:#ff4444}
.luck8-label{font-size:18px;font-weight:bold;letter-spacing:1px}
.luck8-tai .luck8-label{color:#00ff88;text-shadow:0 0 10px rgba(0,255,136,0.5)}
.luck8-xiu .luck8-label{color:#ff4444;text-shadow:0 0 10px rgba(255,68,68,0.5)}
.luck8-circle.blink{animation:blink 1s ease-in-out infinite}
@keyframes blink{0%,100%{transform:scale(1);box-shadow:0 0 0 0 rgba(255,255,255,0.6)}50%{transform:scale(1.12);box-shadow:0 0 0 15px rgba(255,255,255,0);filter:brightness(1.4)}}
.luck8-history{background:rgba(15,35,60,0.6);border-radius:15px;padding:15px;border:1px solid rgba(79,195,247,0.25);max-height:250px;overflow-y:auto}
.luck8-history-title{color:#4fc3f7;font-size:14px;font-weight:bold;margin-bottom:12px;text-align:center;text-transform:uppercase;letter-spacing:1px}
.luck8-history-item{display:flex;justify-content:space-between;align-items:center;padding:10px;background:rgba(20,40,70,0.5);border-radius:8px;margin-bottom:8px;border:1px solid rgba(79,195,247,0.15);font-size:13px}
.luck8-history-item:last-child{margin-bottom:0}
.luck8-history-session{color:#81d4fa;font-weight:600;flex:0 0 80px}
.luck8-history-col{display:flex;flex-direction:column;align-items:center;flex:1}
.luck8-history-label{color:#81d4fa;font-size:10px;margin-bottom:3px;text-transform:uppercase}
.luck8-history-value{font-weight:bold;font-size:14px}
.luck8-history-status{font-size:16px;flex:0 0 30px;text-align:center}
.luck8-history::-webkit-scrollbar{width:6px}
.luck8-history::-webkit-scrollbar-track{background:rgba(20,40,70,0.3);border-radius:6px}
.luck8-history::-webkit-scrollbar-thumb{background:rgba(79,195,247,0.5);border-radius:6px}
.luck8-history::-webkit-scrollbar-thumb:hover{background:rgba(79,195,247,0.7)}

/* New Robot UI */
.draggable-box{position:fixed;top:15px;left:15px;display:flex;align-items:center;gap:12px;z-index:9999;touch-action:none;user-select:none;-webkit-user-select:none;}
.robot-container{width:66px;height:66px;animation:float 3s ease-in-out infinite;}
.robot-avatar{width:100%;border-radius:50%;box-shadow:none;}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}
.action-btns{position:absolute;top:-18px;left:-10px;display:flex;gap:5px;z-index:10001}
.action-btn{width:24px;height:24px;border-radius:50%;border:none;background:rgba(13,31,54,0.9);color:#00e6b4;font-weight:bold;cursor:pointer;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 5px rgba(0,0,0,0.5);border:1px solid rgba(0,230,180,0.3);transition:all 0.2s}
.action-btn:hover{transform:scale(1.1);background:#00e6b4;color:#000}
.robot-avatar{transition:transform 0.3s ease}

.prediction-box{
background:rgba(10, 25, 45, 0.9);
backdrop-filter:blur(10px);
padding:10px 15px;
border-radius:16px;
min-width:auto;
box-shadow:0 5px 20px rgba(0,0,0,0.5);
border:1px solid rgba(0, 230, 180, 0.3);
transition:all 0.4s ease;
display:flex;
flex-direction:column;
gap:4px;
}
.session-info{font-size:12px;font-weight:600;color:#88ccff;text-align:left;text-transform:uppercase;letter-spacing:0.5px;margin:0}
.waiting{color:#fff;font-size:13px;font-weight:600;text-align:left;margin:0}
.confidence{font-size:11px;font-weight:500;text-align:left;color:#00e6b4;margin:0}
.typing-cursor::after{content:'|';animation:blinkCursor 0.8s infinite;color:#00e6b4;margin-left:2px}
@keyframes blinkCursor{0%,100%{opacity:1}50%{opacity:0}}

.history-mini{margin-top:5px;max-height:120px;overflow-y:auto;width:100%;display:none;background:rgba(0,0,0,0.3);border-radius:8px;padding:5px}
.history-mini::-webkit-scrollbar{width:3px}
.history-mini::-webkit-scrollbar-thumb{background:#00e6b4;border-radius:3px}
.h-row{display:flex;justify-content:space-between;align-items:center;font-size:15px;padding:12px 10px;border-bottom:1px solid rgba(255,255,255,0.1);background:rgba(255,255,255,0.02)}
.h-sess{color:#ccc;font-family:monospace;font-size:14px}
.h-win{color:#00ff00;font-weight:900;text-shadow:0 0 10px rgba(0,255,0,0.5)}
.h-lose{color:#ff4444;font-weight:900;text-shadow:0 0 10px rgba(255,68,68,0.5)}
.h-wait{color:#ffff00;font-weight:bold;opacity:0.8}

.controls-container {
    position: fixed;
    bottom: 30px;
    right: 30px;
    display: flex;
    gap: 10px;
    z-index: 9990;
}
.control-btn {
    background: linear-gradient(135deg, #00e6b4, #00b4d8);
    color: #0a1628;
    border: none;
    border-radius: 50px;
    padding: 12px 20px;
    font-weight: bold;
    box-shadow: 0 5px 15px rgba(0, 230, 180, 0.4);
    cursor: pointer;
    transition: transform 0.3s;
    display: flex;
    align-items: center;
    gap: 8px;
}
.control-btn:hover { transform: scale(1.05); box-shadow: 0 8px 20px rgba(0, 230, 180, 0.6); }
.control-btn.inactive { filter: grayscale(1); opacity: 0.7; }

.history-panel {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 90%;
    max-width: 450px;
    background: rgba(10, 25, 45, 0.95);
    border: 1px solid rgba(0, 230, 180, 0.3);
    border-radius: 16px;
    padding: 0;
    z-index: 10000;
    display: none;
    backdrop-filter: blur(15px);
    box-shadow: 0 20px 60px rgba(0,0,0,0.8);
    overflow: hidden;
}
.history-header {
    padding: 20px;
    background: rgba(0, 230, 180, 0.1);
    border-bottom: 1px solid rgba(0, 230, 180, 0.2);
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.history-title { font-weight: bold; color: #00e6b4; font-size: 20px; text-transform:uppercase; letter-spacing:1px }
.history-close { background: none; border: none; color: #fff; font-size: 24px; cursor: pointer; line-height: 1; }
.history-content {
    max-height: 350px;
    overflow-y: auto;
    padding: 10px;
}
.history-content::-webkit-scrollbar { width: 4px; }
.history-content::-webkit-scrollbar-thumb { background: #00e6b4; border-radius: 4px; }

@media(max-width:600px){
.draggable-box{top:70px;left:10px;gap:8px}
.robot-container{width:50px;height:50px}
.prediction-box{padding:8px 12px;border-radius:12px}
.session-info{font-size:11px}
.waiting{font-size:12px}
.confidence{font-size:10px}
.action-btns{top:-15px;left:-5px}
.action-btn{width:22px;height:22px;font-size:12px}
.controls-container{bottom:20px;right:15px;gap:8px}
.control-btn{padding:10px 16px;font-size:13px}
.history-panel{width:95%}
.history-content{max-height:50vh}
}
</style>
<script>
let gameCode='{{gcode}}';
let lastSession=null;
let lastPredictedSession=null; // Lưu phiên đã dự đoán
let lastPrediction=null; // Lưu dự đoán cuối cùng
let isPredicting=false; // Trạng thái đang dự đoán

async function refresh(){
try{
let r=await fetch("/api/predict/"+gameCode);
let j=await r.json();
if(j.ok && j.result){
if(gameCode==='sun' || gameCode==='789' || gameCode==='68gb' || gameCode==='lc79'){
updateGenericGame(j.result);
}else if(gameCode==='sicbo'){
updateSicbo(j.result);
}else if(gameCode==='sum'){
updateSumClub(j.result);
}else if(gameCode==='luck8'){
updateLuck8(j.result);
}else{
updateHitB52(j.result);
}
}
}catch(e){console.error(e)}
}

function triggerRobotEffect(){
let r=document.getElementById("robotAvatar");
if(r){
r.classList.remove("robot-flash");
void r.offsetWidth;
r.classList.add("robot-flash");
}
}

function typeWriter(element, text, finalHtml) {
    element.innerHTML = "";
    element.classList.add("typing-cursor");
    let i = 0;
    let speed = 50; // Tốc độ gõ (ms)
    function type() {
        if (i < text.length) {
            element.textContent += text.charAt(i);
            i++;
            setTimeout(type, speed);
        } else {
            element.innerHTML = finalHtml;
            element.classList.remove("typing-cursor");
        }
    }
    type();
}

function toggleRobot(){
    let box = document.getElementById('dragBox');
    let btn = document.getElementById('robotBtn');
    if(box){
        if(box.style.display === 'none'){
            box.style.display = 'flex';
            if(btn) btn.classList.remove('inactive');
        } else {
            box.style.display = 'none';
            if(btn) btn.classList.add('inactive');
        }
    }
}

let robotRotation = 0;
function rotateRobot(){
    robotRotation += 90;
    let avatar = document.getElementById("robotAvatar");
    if(avatar){
        avatar.style.transform = `rotate(${robotRotation}deg)`;
    }
}

function toggleHistoryPanel(){
    let h = document.getElementById('historyPanel');
    if(h.style.display === 'none' || h.style.display === ''){
        h.style.display = 'block';
    } else {
        h.style.display = 'none';
    }
}

function renderHistory(history){
    let el = document.getElementById('full-history-list');
    if(!el || !history) return;
    let html = '';
    history.forEach(h => {
        // Tự tính toán trạng thái nếu server chưa trả về correct nhưng đã có kết quả
        let isCorrect = h.correct;
        if (isCorrect === null || isCorrect === undefined) {
            if (h.result && h.prediction && (h.result === "Tài" || h.result === "Xỉu")) {
                isCorrect = (h.result === h.prediction);
            }
        }

        let resClass = isCorrect === true ? 'h-win' : (isCorrect === false ? 'h-lose' : 'h-wait');
        let resText = isCorrect === true ? 'THẮNG' : (isCorrect === false ? 'THUA' : '???');
        let actual = h.result ? h.result : '?';
        html += `<div class="h-row"><span class="h-sess">#${h.session}</span><span style="font-weight:bold;color:#fff">${h.prediction} ➔ ${actual}</span><span class="${resClass}">${resText}</span></div>`;
    });
    el.innerHTML = html;
}

function updateRobotUI(phien, pred, conf){
    let sessionInfo = document.getElementById("session-info-text");
    let waitingText = document.getElementById("waiting-text");
    let confidenceBox = document.getElementById("confidence-box");
    let confidenceText = document.getElementById("confidence");

    if(!sessionInfo) return;

    if(!phien || phien==="---" || phien==="N/A" || phien==="—"){
        sessionInfo.innerHTML = "Đang kết nối...";
        waitingText.innerHTML = "Đang tải dữ liệu...";
        confidenceBox.style.display = "none";
        return;
    }

    let phienTiepTheo = parseInt(phien) + 1;
    sessionInfo.innerHTML = `Phiên: #${phienTiepTheo}`;
    sessionInfo.style.display = "block";

    let confPercent = conf ? Math.round(conf*100) : 72;

    if(pred && (pred==="Tài" || pred==="Xỉu")){
        let color = pred==="Tài" ? "#00ff00" : "#ff4444";
        let fullHtml = `Dự đoán: <span style="color:${color};font-size:26px;font-weight:900;text-shadow:0 0 15px ${color}">${pred}</span>`;
        if (waitingText.getAttribute('data-last') !== pred) {
            typeWriter(waitingText, `Dự đoán: ${pred}`, fullHtml);
            waitingText.setAttribute('data-last', pred);
        } else {
            waitingText.innerHTML = fullHtml;
        }
        confidenceText.innerHTML = `${confPercent}%`;
        confidenceText.style.color = confPercent > 70 ? "#00ff00" : "#ffaa00";
        confidenceBox.style.display = "block";
    }else{
        waitingText.innerHTML = "Đang chờ kết quả...";
        confidenceBox.style.display = "none";
    }
}

function updateGenericGame(data){
let sessionInfo = document.getElementById("session-info-text");
let waitingText = document.getElementById("waiting-text");
let confidenceBox = document.getElementById("confidence-box");
let confidenceText = document.getElementById("confidence");

if(!sessionInfo) return;

let phien=data.phien;
let pred=data.du_doan_tiep_theo || data.du_doan;
let conf=data.do_tin_cay || 0.72;
let confPercent=Math.round(conf*100);

if(!phien || phien==="---"){
sessionInfo.innerHTML = "Đang kết nối...";
waitingText.innerHTML = "Đang tải dữ liệu...";
confidenceBox.style.display = "none";
return;
}

let phienTiepTheo = parseInt(phien) + 1;
sessionInfo.innerHTML = `Phiên: #${phienTiepTheo}`;
sessionInfo.style.display = "block";

if(lastSession !== phien){
lastSession = phien;
lastPredictedSession = null;
triggerRobotEffect();
}

if(pred && (pred==="Tài" || pred==="Xỉu")){
let color = pred==="Tài" ? "#00ff00" : "#ff4444";
let fullHtml = `Dự đoán: <span style="color:${color};font-size:26px;font-weight:900;text-shadow:0 0 15px ${color}">${pred}</span>`;
if (waitingText.getAttribute('data-last') !== pred) {
    typeWriter(waitingText, `Dự đoán: ${pred}`, fullHtml);
    waitingText.setAttribute('data-last', pred);
} else {
    waitingText.innerHTML = fullHtml;
}
confidenceText.innerHTML = `${confPercent}%`;
confidenceText.style.color = confPercent > 70 ? "#00ff00" : "#ffaa00";
confidenceBox.style.display = "block";
lastPredictedSession = phien;
}else{
waitingText.innerHTML = "Đang chờ kết quả...";
confidenceBox.style.display = "none";
}

if(data.history) renderHistory(data.history);
}

function updateSicbo(data){
let sessionInfo = document.getElementById("session-info-text");
let waitingText = document.getElementById("waiting-text");
let confidenceBox = document.getElementById("confidence-box");
let confidenceText = document.getElementById("confidence");

if(!sessionInfo) return;

let phienHienTai=data.phien_hien_tai;
let phienTiepTheo=data.phien_tiep_theo;
let pred=data.du_doan;
let conf=data.do_tin_cay || 63;
let confPercent=typeof conf === 'number' ? conf : parseInt(conf);
let viDuDoan=data.vi_du_doan || [10,11,12];

if(!phienTiepTheo || phienTiepTheo==="---"){
sessionInfo.innerHTML = "Đang kết nối...";
waitingText.innerHTML = "Đang tải dữ liệu...";
confidenceBox.style.display = "none";
return;
}

sessionInfo.innerHTML = `Phiên: #${phienTiepTheo}`;
sessionInfo.style.display = "block";

if(lastSession !== phienHienTai){
lastSession = phienHienTai;
lastPredictedSession = null;
triggerRobotEffect();
}

if(pred && (pred==="Tài" || pred==="Xỉu")){
let color = pred==="Tài" ? "#00ff00" : "#ff4444";
let viText = viDuDoan.length > 0 ? `<br><span style="font-size:12px;color:#00e6b4">Vị: ${viDuDoan.join(', ')}</span>` : "";
let fullHtml = `Dự đoán: <span style="color:${color};font-size:26px;font-weight:900;text-shadow:0 0 15px ${color}">${pred}</span>${viText}`;
if (waitingText.getAttribute('data-last') !== pred) {
    typeWriter(waitingText, `Dự đoán: ${pred}`, fullHtml);
    waitingText.setAttribute('data-last', pred);
} else {
    waitingText.innerHTML = fullHtml;
}
confidenceText.innerHTML = `${confPercent}%`;
confidenceBox.style.display = "block";
lastPredictedSession = phienHienTai;
}else{
waitingText.innerHTML = "Đang chờ kết quả...";
confidenceBox.style.display = "none";
}

if(data.history) renderHistory(data.history);
}

function updateSumClub(data){
let widget=document.getElementById("widget");
let sessionEl=document.getElementById("sumSession");
let dotTai=document.getElementById("dotTai");
let dotXiu=document.getElementById("dotXiu");
if(!sessionEl) return;

let session=data.phien || "—";
let result=data.du_doan || "";

// Tính phiên tiếp theo
let sessionTiepTheo = session !== "—" ? (parseInt(session) + 1) : "—";

// Khi có phiên mới, reset và hiệu ứng shake
if(session!==lastSession && lastSession!==null){
lastSession=session;
widget.classList.add("shake");
triggerRobotEffect();
setTimeout(()=>widget.classList.remove("shake"),500);
// Reset dot về màu đen khi có phiên mới
dotTai.className="dot";
dotXiu.className="dot";
}
lastSession=session;

// Hiển thị phiên tiếp theo
sessionEl.textContent=sessionTiepTheo;

// Chỉ hiển thị và nháy khi có dự đoán rõ ràng
if(result==="Tài"){
// Tài nháy xanh liên tục
dotTai.className="dot on-green blink";
// Xỉu hoàn toàn tối (không có class on-red)
dotXiu.className="dot";
}else if(result==="Xỉu"){
// Xỉu nháy đỏ liên tục
dotXiu.className="dot on-red blink";
// Tài hoàn toàn tối (không có class on-green)
dotTai.className="dot";
}else{
// Không có dự đoán - giữ 2 bên màu đen hoàn toàn
dotTai.className="dot";
dotXiu.className="dot";
}

// Update Robot UI
updateRobotUI(session, result, data.do_tin_cay);
}

function updateHitB52(data){
let phienEl=document.getElementById("phienText");
let predEl=document.getElementById("prediction");
let resultEl=document.getElementById("result");
let statusEl=document.getElementById("status");
if(!phienEl) return;

// Tính phiên tiếp theo
let phien = data.phien || "N/A";
let phienTiepTheo = phien !== "N/A" ? (parseInt(phien) + 1) : "N/A";

if(phien!=="N/A" && lastSession!==phien){
lastSession=phien;
triggerRobotEffect();
}
phienEl.textContent="#"+phienTiepTheo;
let pred=data.du_doan || "N/A";
let color=pred==="Tài"?"#00ff00":"#ff4444";
predEl.innerHTML=`<span style="color:${color};text-shadow:0 0 15px ${color};">${pred}</span>`;
resultEl.textContent=data.ket_qua || "Đang chờ...";
statusEl.innerHTML='<span style="color:#00ff00">●</span> Đã kết nối';

if(data.history) renderHistory(data.history);

// Update Robot UI
updateRobotUI(phien, pred, data.do_tin_cay);
}

let luck8History=[];

function updateLuck8(data){
let sessionEl=document.getElementById("luck8Session");
let taiCircle=document.getElementById("taiCircle");
let xiuCircle=document.getElementById("xiuCircle");
if(!sessionEl) return;

let session=data.phien || "---";
let pred=data.du_doan || "";
let result=data.ket_qua || "";

// Tính phiên tiếp theo
let sessionTiepTheo = session !== "---" ? (parseInt(session) + 1) : "---";
sessionEl.innerHTML=`Phiên: <span>#${sessionTiepTheo}</span>`;

// Reset circles và lưu lịch sử khi có phiên mới
if(session!==lastSession && lastSession!==null){
// Lưu kết quả phiên trước vào lịch sử
if(lastPredictedSession && lastPrediction && result && (result==="Tài" || result==="Xỉu")){
let prevSessionDisplay = lastPredictedSession !== "---" ? (parseInt(lastPredictedSession) + 1) : "---";
let isCorrect = lastPrediction === result;
luck8History.unshift({
session: prevSessionDisplay,
prediction: lastPrediction,
result: result,
isCorrect: isCorrect
});
// Giữ tối đa 10 phiên
if(luck8History.length > 10) luck8History.pop();
updateLuck8History();
// Tự động lưu lịch sử lên server và localStorage
saveLuck8HistoryToServer();
saveToLocalStorage();
}

lastSession=session;
lastPredictedSession=null;
lastPrediction=null;
taiCircle.className="luck8-circle luck8-tai";
xiuCircle.className="luck8-circle luck8-xiu";
triggerRobotEffect();
}
lastSession=session;

// Hiển thị dự đoán
if(pred==="Tài"){
taiCircle.className="luck8-circle luck8-tai blink";
xiuCircle.className="luck8-circle luck8-xiu";
lastPredictedSession=session;
lastPrediction="Tài";
}else if(pred==="Xỉu"){
xiuCircle.className="luck8-circle luck8-xiu blink";
taiCircle.className="luck8-circle luck8-tai";
lastPredictedSession=session;
lastPrediction="Xỉu";
}else{
taiCircle.className="luck8-circle luck8-tai";
xiuCircle.className="luck8-circle luck8-xiu";
}

// Update Robot UI
updateRobotUI(session, pred, data.do_tin_cay);
}

function updateLuck8History(){
let historyEl=document.getElementById("luck8HistoryList");
if(!historyEl) return;

if(luck8History.length===0){
historyEl.innerHTML='<div style="text-align:center;color:#81d4fa;padding:15px;font-size:12px">Chưa có lịch sử</div>';
return;
}

let html='';
luck8History.slice(0,10).forEach(item=>{
let predColor=item.prediction==="Tài"?"#00ff88":"#ff4444";
let resultColor=item.result==="Tài"?"#00ff88":"#ff4444";
let statusIcon=item.isCorrect?"✅":"❌";

html+=`<div class="luck8-history-item">
<div class="luck8-history-session">#${item.session}</div>
<div class="luck8-history-col">
<div class="luck8-history-label">Dự đoán</div>
<div class="luck8-history-value" style="color:${predColor}">${item.prediction}</div>
</div>
<div class="luck8-history-col">
<div class="luck8-history-label">Kết quả</div>
<div class="luck8-history-value" style="color:${resultColor}">${item.result}</div>
</div>
<div class="luck8-history-status">${statusIcon}</div>
</div>`;
});

historyEl.innerHTML=html;
}

// Lưu lịch sử vào localStorage
function saveToLocalStorage(){
try{
localStorage.setItem('luck8_history',JSON.stringify(luck8History));
console.log('✅ Đã lưu lịch sử vào localStorage');
}catch(e){
console.error('❌ Lỗi lưu localStorage:',e);
}
}

// Tải lịch sử từ localStorage khi load trang
function loadFromLocalStorage(){
try{
let saved=localStorage.getItem('luck8_history');
if(saved){
luck8History=JSON.parse(saved);
updateLuck8History();
console.log(`✅ Đã tải ${luck8History.length} phiên từ localStorage`);
}
}catch(e){
console.error('❌ Lỗi tải localStorage:',e);
}
}

async function saveLuck8HistoryToServer(){
if(luck8History.length===0) return;
try{
await fetch('/api/save-luck8-history',{
method:'POST',
headers:{'Content-Type':'application/json'},
body:JSON.stringify({history:luck8History})
});
console.log('✅ Đã lưu lịch sử lên server');
}catch(e){
console.error('❌ Lỗi lưu lịch sử lên server:',e);
}
}

function updateTime(){
let now=new Date();
let h=now.getHours().toString().padStart(2,'0');
let m=now.getMinutes().toString().padStart(2,'0');
let s=now.getSeconds().toString().padStart(2,'0');
let clockEl=document.getElementById("clock");
if(clockEl) clockEl.textContent=h+':'+m+':'+s;
}

// Tải lịch sử từ localStorage khi khởi động (chỉ cho Luck8)
if(gameCode==='luck8'){
loadFromLocalStorage();
}

setInterval(refresh,3000);
if(gameCode==='hit' || gameCode==='b52' || gameCode==='luck8'){
setInterval(updateTime,1000);
}
refresh();
if(gameCode==='hit' || gameCode==='b52' || gameCode==='luck8'){
updateTime();
}

if(gameCode!=='sun' && gameCode!=='sum' && gameCode!=='luck8'){
particlesJS("particles-js",{
particles:{
number:{value:120,density:{enable:true,value_area:800}},
color:{value:["#00ffff","#00aaff","#0088ff","#ffffff"]},
shape:{type:"circle",stroke:{width:0,color:"#000000"}},
opacity:{value:0.7,random:true,anim:{enable:true,speed:1,opacity_min:0.1,sync:false}},
size:{value:3,random:true,anim:{enable:true,speed:2,size_min:0.1,sync:false}},
line_linked:{enable:true,distance:150,color:"#00aaff",opacity:0.3,width:1},
move:{enable:true,speed:1,direction:"none",random:true,straight:false,out_mode:"out",bounce:false,attract:{enable:true,rotateX:600,rotateY:1200}}
},
interactivity:{
detect_on:"canvas",
events:{onhover:{enable:true,mode:"bubble"},onclick:{enable:true,mode:"push"},resize:true},
modes:{bubble:{distance:200,size:6,duration:2,opacity:0.8,speed:3},push:{particles_nb:4}}
},
retina_detect:true
});
}

// Cho phép kéo thả Robot mới
document.addEventListener("DOMContentLoaded", function() {
    dragElement(document.getElementById("dragBox"));
    if(gameCode==='sum') dragElement(document.getElementById("widget"));
});

function dragElement(elmnt){
if(!elmnt) return;
let startX=0,startY=0,initialLeft=0,initialTop=0;

// Thêm style cho cursor
elmnt.style.cursor='grab';
elmnt.style.touchAction = 'none';
elmnt.style.userSelect = 'none';
elmnt.style.position = 'fixed';

// Mouse events
elmnt.onmousedown=dragMouseDown;
// Touch events
elmnt.addEventListener('touchstart', dragTouchStart, {passive: false});

function dragMouseDown(e){
    e=e||window.event;
    // Cho phép click vào nút đóng hoặc các nút khác
    if(e.target.tagName==='BUTTON' || e.target.closest('button')) return;
    
    e.preventDefault();
    startX=e.clientX;
    startY=e.clientY;
    let rect = elmnt.getBoundingClientRect();
    initialLeft=rect.left;
    initialTop=rect.top;
    
    elmnt.style.cursor='grabbing';
    elmnt.style.opacity='0.8';
    document.onmouseup=closeDragElement;
    document.onmousemove=elementDrag;
}

function elementDrag(e){
    e=e||window.event;
    e.preventDefault();
    let dx=e.clientX-startX;
    let dy=e.clientY-startY;
    elmnt.style.top=(initialTop+dy)+"px";
    elmnt.style.left=(initialLeft+dx)+"px";
    elmnt.style.bottom='auto';
    elmnt.style.right='auto';
}

function dragTouchStart(e){
    if(e.target.tagName==='BUTTON' || e.target.closest('button')) return;
    
    if(e.cancelable) e.preventDefault();
    let touch=e.touches[0];
    startX=touch.clientX;
    startY=touch.clientY;
    let rect = elmnt.getBoundingClientRect();
    initialLeft=rect.left;
    initialTop=rect.top;
    
    elmnt.style.opacity='0.8';
    document.addEventListener('touchend', closeDragElement, {passive: false});
    document.addEventListener('touchmove', elementTouchDrag, {passive: false});
}

function elementTouchDrag(e){
    if(e.cancelable) e.preventDefault();
    let touch=e.touches[0];
    let dx=touch.clientX-startX;
    let dy=touch.clientY-startY;
    elmnt.style.top=(initialTop+dy)+"px";
    elmnt.style.left=(initialLeft+dx)+"px";
    elmnt.style.bottom='auto';
    elmnt.style.right='auto';
}

function closeDragElement(){
    document.onmouseup=null;
    document.onmousemove=null;
    document.removeEventListener('touchend', closeDragElement);
    document.removeEventListener('touchmove', elementTouchDrag);
    elmnt.style.cursor='grab';
    elmnt.style.opacity='1';
}
}
</script>
</head>
<body>
<div id="particles-js"></div>
<div class="header">
<div class="game-title">🎲 {{game}}</div>
<a href="/menu" class="back-btn">← Menu</a>
</div>

<div class="iframe-container" id="sunContainer" style="display:{% if gcode=='sun' or gcode=='sicbo' %}block{% else %}none{% endif %}">
<iframe src="https://web.sunwin.sx/?affId=Sunwin"></iframe>
</div>
<div class="iframe-container" id="789Container" style="display:{% if gcode=='789' %}block{% else %}none{% endif %}">
<iframe src="https://play.789club.cc/?affId=789"></iframe>
</div>
<div class="iframe-container" id="68gbContainer" style="display:{% if gcode=='68gb' %}block{% else %}none{% endif %}">
<iframe src="https://68gbvn88.bar/"></iframe>
</div>
<div class="iframe-container" id="lc79Container" style="display:{% if gcode=='lc79' %}block{% else %}none{% endif %}">
<iframe src="https://play.lc79.bet/"></iframe>
</div>

<div class="draggable-box" id="dragBox" style="display:{% if gcode == 'hit' or gcode == 'b52' %}none{% else %}flex{% endif %}">
  <div class="action-btns">
    <button class="action-btn" onclick="toggleRobot()">×</button>
    <button class="action-btn" onclick="rotateRobot()">↻</button>
  </div>
  <div class="robot-container">
    <img src="https://i.postimg.cc/1zLnNsCZ/IMG-3575.gif" alt="AI" class="robot-avatar" id="robotAvatar">
  </div>
  <div class="prediction-box">
    <div class="session-info" id="session-info-text" style="display: none;">Đang khởi động AI...</div>
    <div class="waiting" id="waiting-text" style="display: block;">Đang chờ phiên tiếp theo...</div>
    <div class="confidence" id="confidence-box" style="display:none;">
      Độ tin cậy: <span id="confidence" style="color:#ff3333;">--%</span>
    </div>
  </div>
</div>

<div class="widget" id="widget" style="display:{% if gcode=='sum' %}flex{% else %}none{% endif %}">
<div class="session">Phiên tiếp theo: <span id="sumSession">—</span></div>
<div class="row">
<div class="side">
<div class="dot" id="dotTai"></div>
<span>Tài</span>
</div>
<div class="center-logo">
<img src="https://i.postimg.cc/C1gt9QB0/IMG-1593.jpg" alt="SumClub">
</div>
<div class="side">
<div class="dot" id="dotXiu"></div>
<span>Xỉu</span>
</div>
</div>
</div>

<div class="wrapper" id="hitb52Container" style="display:{% if gcode=='hit' or gcode=='b52' %}block{% else %}none{% endif %}">
<h2 class="game-title-main">
<span class="float-1">DỰ</span>
<span class="float-2">ĐOÁN</span>
<span class="float-3">TÀI</span>
<span class="float-4">XỈU</span>
</h2>
<div class="prediction-box">
<div class="prediction-item">
<div class="label">Phiên tiếp theo</div>
<div class="value" id="phienText">#---</div>
</div>
<div class="prediction-item">
<div class="label">Dự đoán</div>
<div class="value prediction-value" id="prediction">--</div>
</div>
</div>
<div class="status-info">
<div class="status-row">
<span class="stat-label">📊 Kết quả trước:</span>
<span class="stat-value" id="result">Đang chờ...</span>
</div>
<div class="status-row">
<span class="stat-label">🔗 Trạng thái:</span>
<span class="stat-value" id="status">Đang kết nối...</span>
</div>
<div class="status-row">
<span class="stat-label">🕐 Thời gian:</span>
<span class="stat-value" id="clock">--:--:--</span>
</div>
</div>
</div>

<div class="luck8-container" id="luck8Container" style="display:{% if gcode=='luck8' %}block{% else %}none{% endif %}">
<div class="luck8-session" id="luck8Session">Phiên: <span>#---</span></div>
<div class="luck8-circle-container">
<div class="luck8-circle luck8-tai" id="taiCircle">
<i class="fas fa-arrow-up luck8-icon"></i>
<div class="luck8-label">TÀI</div>
</div>
<div class="luck8-circle luck8-xiu" id="xiuCircle">
<i class="fas fa-arrow-down luck8-icon"></i>
<div class="luck8-label">XỈU</div>
</div>
</div>
<div class="luck8-history">
<div class="luck8-history-title">📊 Lịch sử</div>
<div id="luck8HistoryList">
<div style="text-align:center;color:#81d4fa;padding:15px;font-size:12px">Chưa có lịch sử</div>
</div>
</div>
</div>

<div class="controls-container" style="display:{% if gcode == 'hit' or gcode == 'b52' %}none{% else %}flex{% endif %}">
    <button class="control-btn" id="robotBtn" onclick="toggleRobot()"><i class="fas fa-robot"></i> Robot</button>
    <button class="control-btn" onclick="toggleHistoryPanel()"><i class="fas fa-history"></i> Lịch sử</button>
</div>

<div id="historyPanel" class="history-panel">
    <div class="history-header">
        <span class="history-title">📜 Lịch Sử Dự Đoán</span>
        <button class="history-close" onclick="toggleHistoryPanel()">×</button>
    </div>
    <div id="full-history-list" class="history-content">
        <div style="text-align:center;color:#aaa;padding:20px">Chưa có dữ liệu</div>
    </div>
</div>
</body>
</html>"""


