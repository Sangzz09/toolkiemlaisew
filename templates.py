# -*- coding: utf-8 -*-
# ================== templates.py ==================
# Load HTML templates từ các file riêng biệt

import os

# Thư mục gốc (nơi chứa templates.py và các file game HTML)
_root = os.path.dirname(os.path.abspath(__file__))

# Thư mục chứa các page template thông thường
_tpl_dir = os.path.join(_root, 'templates')

def _load(filename, subdir=True):
    """Load file HTML. subdir=True → tìm trong /templates/, False → tìm ở thư mục gốc."""
    folder = _tpl_dir if subdir else _root
    path = os.path.join(folder, filename)
    if not os.path.exists(path):
        # Fallback: thử tìm ở cả 2 nơi
        alt = os.path.join(_root if subdir else _tpl_dir, filename)
        if os.path.exists(alt):
            path = alt
        else:
            raise FileNotFoundError(f"Không tìm thấy template: {filename}")
    with open(path, encoding='utf-8') as f:
        return f.read()

# ── Page templates (nằm trong thư mục templates/) ──────────────────────────
HTML_REGISTER       = _load('register.html')
HTML_LOGIN          = _load('login.html')
HTML_MENU           = _load('menu.html')
HTML_ACCOUNT        = _load('account.html')
HTML_BUY_KEY        = _load('buy_key.html')
HTML_DEPOSIT        = _load('deposit.html')
HTML_DEPOSIT_SEPAY  = HTML_DEPOSIT   # alias
HTML_ENTER_KEY      = _load('enter_key.html')

# ── Game templates (nằm ở thư mục gốc, cùng cấp với templates.py) ──────────
HTML_GAME_SUN       = _load('game_sun.html',   subdir=False)
HTML_GAME_HIT       = _load('game_hit.html',   subdir=False)
HTML_GAME_B52       = _load('game_b52.html',   subdir=False)
HTML_GAME_SICBO     = _load('game_sicbo.html', subdir=False)
HTML_GAME_789       = _load('game_789.html',   subdir=False)
HTML_GAME_68GB      = _load('game_68gb.html',  subdir=False)
HTML_GAME_LUCK8     = _load('game_luck8.html', subdir=False)
HTML_GAME_LC79      = _load('game_lc79.html',  subdir=False)

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
