# -*- coding: utf-8 -*-
# ================== templates.py ==================
# Load HTML templates từ các file riêng biệt
# FIX: Tất cả file HTML nằm ở thư mục gốc (không có thư mục con templates/)

import os

# Thư mục gốc (nơi chứa tất cả file HTML)
_root = os.path.dirname(os.path.abspath(__file__))

def _load(filename):
    """Load file HTML từ thư mục gốc."""
    path = os.path.join(_root, filename)
    if not os.path.exists(path):
        raise FileNotFoundError(f"Không tìm thấy template: {filename} (đường dẫn: {path})")
    with open(path, encoding='utf-8') as f:
        return f.read()

# ── Page templates ──────────────────────────────────────────────────────────
HTML_REGISTER       = _load('register.html')
HTML_LOGIN          = _load('login.html')
HTML_MENU           = _load('menu.html')
HTML_ACCOUNT        = _load('account.html')
HTML_BUY_KEY        = _load('buy_key.html')
HTML_DEPOSIT        = _load('deposit.html')
HTML_DEPOSIT_SEPAY  = HTML_DEPOSIT   # alias
HTML_ENTER_KEY      = _load('enter_key.html')

# ── Game templates ──────────────────────────────────────────────────────────
HTML_GAME_SUN       = _load('game_sun.html')
HTML_GAME_HIT       = _load('game_hit.html')
HTML_GAME_B52       = _load('game_b52.html')
HTML_GAME_SICBO     = _load('game_sicbo.html')
HTML_GAME_789       = _load('game_789.html')
HTML_GAME_68GB      = _load('game_68gb.html')
HTML_GAME_LUCK8     = _load('game_luck8.html')
HTML_GAME_LC79      = _load('game_lc79.html')

# ── Map gcode → template (dùng trong route /game/<gcode>) ──────────────────
GAME_TEMPLATES = {
    'sun':   HTML_GAME_SUN,
    'hit':   HTML_GAME_HIT,
    'b52':   HTML_GAME_B52,
    'sicbo': HTML_GAME_SICBO,
    '789':   HTML_GAME_789,
    '68gb':  HTML_GAME_68GB,
    'luck8': HTML_GAME_LUCK8,
    'lc79':  HTML_GAME_LC79,
}
