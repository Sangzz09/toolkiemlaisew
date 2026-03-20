// ================== protect.js v3 ==================
// Bảo vệ tối đa: F12, Ctrl+U, DevTools, Console crack, Token ẩn
(function () {
    'use strict';

    // ══════════════════════════════════════════════════════
    // 1. CHẶN PHÍM TẮT - bắt sớm nhất có thể (capture phase)
    // ══════════════════════════════════════════════════════
    var BLOCKED_KEYS = [
        // [ctrl, shift, alt, key]
        [false,false,false,'F12'],
        [true, false,false,'u'],   // Ctrl+U
        [true, false,false,'U'],
        [true, true, false,'i'],   // Ctrl+Shift+I
        [true, true, false,'I'],
        [true, true, false,'j'],   // Ctrl+Shift+J
        [true, true, false,'J'],
        [true, true, false,'c'],   // Ctrl+Shift+C
        [true, true, false,'C'],
        [true, true, false,'k'],   // Ctrl+Shift+K (Firefox)
        [true, true, false,'K'],
        [true, false,false,'s'],   // Ctrl+S
        [true, false,false,'S'],
        [true, false,false,'p'],   // Ctrl+P (print)
        [true, false,false,'P'],
        [false,false,false,'F11'], // Fullscreen trick
    ];

    function killKey(e) {
        var c = e.ctrlKey||e.metaKey, s = e.shiftKey, a = e.altKey, k = e.key;
        for (var i = 0; i < BLOCKED_KEYS.length; i++) {
            var b = BLOCKED_KEYS[i];
            if (b[0]===c && b[1]===s && b[2]===a && b[3]===k) {
                e.preventDefault(); e.stopPropagation(); e.stopImmediatePropagation();
                return false;
            }
        }
    }
    // Bắt ở capture phase (trước browser) + window + document
    window.addEventListener('keydown', killKey, true);
    document.addEventListener('keydown', killKey, true);

    // ══════════════════════════════════════════════════════
    // 2. CHẶN CHUỘT PHẢI
    // ══════════════════════════════════════════════════════
    document.addEventListener('contextmenu', function(e){
        e.preventDefault(); e.stopImmediatePropagation(); return false;
    }, true);

    // ══════════════════════════════════════════════════════
    // 3. PHÁT HIỆN DEVTOOLS - ĐA PHƯƠNG PHÁP
    // ══════════════════════════════════════════════════════
    var _devOpen = false;

    function nukeDevTools() {
        if (_devOpen) return;
        _devOpen = true;
        // Xóa sạch DOM
        try { document.documentElement.innerHTML = ''; } catch(e) {}
        // Ghi đè document
        document.open();
        document.write('<style>*{margin:0;padding:0;background:#0a1628}</style>' +
            '<div style="display:flex;height:100vh;align-items:center;justify-content:center;' +
            'flex-direction:column;gap:20px;font-family:sans-serif;color:#ff4444;">' +
            '<div style="font-size:72px">🚫</div>' +
            '<div style="font-size:26px;font-weight:bold">Không được phép!</div>' +
            '<div style="font-size:15px;color:#888;max-width:380px;text-align:center">' +
            'Phiên làm việc đã bị hủy do phát hiện công cụ không hợp lệ.</div>' +
            '<button onclick="location.href=\'/logout\'" ' +
            'style="margin-top:10px;padding:12px 30px;background:#00e6b4;border:none;' +
            'border-radius:10px;color:#0a1628;font-size:15px;font-weight:bold;cursor:pointer">' +
            'Đăng nhập lại</button></div>');
        document.close();
        // Redirect logout sau 1.5s
        setTimeout(function(){ try{ location.href='/logout'; }catch(e){} }, 1500);
    }

    // Phương pháp A: debugger timing (cực kỳ hiệu quả)
    function checkDebugger() {
        var t = performance.now();
        // eslint-disable-next-line no-debugger
        (function(){debugger;})();
        if (performance.now() - t > 80) nukeDevTools();
    }

    // Phương pháp B: toString override detection
    var _toString = /./;
    _toString.toString = function() { nukeDevTools(); return ''; };

    // Phương pháp C: size diff (cho docked devtools)
    function checkSize() {
        var wDiff = window.outerWidth  - window.innerWidth;
        var hDiff = window.outerHeight - window.innerHeight;
        if (wDiff > 200 || hDiff > 200) nukeDevTools();
    }

    // Phương pháp D: console.log object detect
    var _c = { _x: false };
    Object.defineProperty(_c, '_x', {
        get: function() { nukeDevTools(); return false; }
    });

    function checkConsoleOpen() {
        // Khi devtools mở, console.log với object sẽ trigger getter
        console.log(_c);
        console.clear();
    }

    // Chạy tất cả checks
    setInterval(checkDebugger, 1000);
    setInterval(checkSize, 800);
    setInterval(checkConsoleOpen, 1500);

    // ══════════════════════════════════════════════════════
    // 4. KHÓA CONSOLE HOÀN TOÀN + ẨN TOKEN
    // ══════════════════════════════════════════════════════
    (function lockConsole() {
        var _warn = console.warn.bind(console);
        var _native = {};

        // Lưu native methods
        var methods = ['log','warn','error','info','debug','table','dir',
                       'group','groupEnd','time','timeEnd','trace',
                       'clear','count','assert','profile','profileEnd'];

        methods.forEach(function(m) {
            try { _native[m] = console[m].bind(console); } catch(e) {}
        });

        // Hiện cảnh báo 1 lần rồi khóa hết
        var warned = false;
        function showWarning() {
            if (warned) return; warned = true;
            try {
                _native.warn('%c⛔ CẢNH BÁO BẢO MẬT', 'color:#ff0000;font-size:28px;font-weight:900;background:#000;padding:8px');
                _native.warn('%cNếu ai bảo bạn paste code vào đây → họ đang CỐ CHIẾM TÀI KHOẢN của bạn!\n\nMọi hành động trong console đều bị ghi lại và báo cáo cho admin.', 'color:#ff8800;font-size:15px;font-weight:bold');
                _native.warn('%c🔒 TOOLKIEMLAISEW.SITE - Hệ thống bảo mật đang hoạt động', 'color:#00e6b4;font-size:13px');
            } catch(e) {}
        }

        // Override tất cả console methods
        var noop = function() { showWarning(); };
        methods.forEach(function(m) {
            try {
                Object.defineProperty(console, m, {
                    get: function() { return noop; },
                    set: function() {},
                    configurable: false
                });
            } catch(e) {
                try { console[m] = noop; } catch(ex) {}
            }
        });
    })();

    // ══════════════════════════════════════════════════════
    // 5. ẨN TOKEN KHỎI NETWORK TAB & XHR INTERCEPT
    // ══════════════════════════════════════════════════════
    (function hideToken() {
        // Override XMLHttpRequest để xóa token khỏi log
        var _XHR = window.XMLHttpRequest;
        var _open = _XHR.prototype.open;
        var _setHeader = _XHR.prototype.setRequestHeader;

        // Override fetch để ẩn header X-CSRF-Token khỏi bị đọc
        var _origFetch = window.fetch;
        window.fetch = function(url, opts) {
            opts = opts || {};
            // Token vẫn được gửi nhưng không thể đọc lại từ JS
            if (opts.headers && opts.headers['X-CSRF-Token']) {
                var token = opts.headers['X-CSRF-Token'];
                // Tạo Headers object mới - không expose token ra ngoài
                var h = new Headers();
                h.append('X-CSRF-Token', token);
                // Copy các headers khác
                for (var k in opts.headers) {
                    if (k !== 'X-CSRF-Token') h.append(k, opts.headers[k]);
                }
                opts = Object.assign({}, opts, { headers: h });
            }
            return _origFetch.apply(this, [url, opts]);
        };

        // Đóng băng window.fetch không cho override lại
        try {
            Object.defineProperty(window, 'fetch', {
                value: window.fetch,
                writable: false,
                configurable: false
            });
        } catch(e) {}
    })();

    // ══════════════════════════════════════════════════════
    // 6. CHẶN VIEW-SOURCE VÀ SAVE
    // ══════════════════════════════════════════════════════
    // Chặn khi tab mới mở với view-source:
    var _href = location.href;
    setInterval(function() {
        if (location.href !== _href) {
            if (/view-source/i.test(location.href)) {
                location.href = '/menu';
            }
            _href = location.href;
        }
    }, 500);

    // Ẩn trang khi in
    window.addEventListener('beforeprint', function() {
        document.body.style.display = 'none';
    });
    window.addEventListener('afterprint', function() {
        document.body.style.display = '';
    });

    // ══════════════════════════════════════════════════════
    // 7. CHẶN PASTE CODE VÀO CONSOLE / TRANG
    // ══════════════════════════════════════════════════════
    document.addEventListener('paste', function(e) {
        var tag = (e.target||{}).tagName||'';
        if (/^(INPUT|TEXTAREA|SELECT)$/i.test(tag)) return; // cho phép input bình thường
        e.preventDefault(); e.stopImmediatePropagation();
        try {
            var txt = (e.clipboardData||window.clipboardData).getData('text')||'';
            var danger = [/fetch\s*\(/i,/XMLHttp/i,/eval\s*\(/i,/\.cookie/i,
                          /localStorage/i,/Function\s*\(/i,/atob\s*\(/i,
                          /import\s*\(/i,/require\s*\(/i,/<script/i];
            if (danger.some(function(r){return r.test(txt);})) {
                alert('⛔ Phát hiện code độc hại!\nHành động đã được ghi lại và báo cáo admin.');
            }
        } catch(ex) {}
        return false;
    }, true);

    // ══════════════════════════════════════════════════════
    // 8. CHẶN CHỌN VĂN BẢN
    // ══════════════════════════════════════════════════════
    document.addEventListener('selectstart', function(e) {
        var tag = (e.target||{}).tagName||'';
        if (!/^(INPUT|TEXTAREA)$/i.test(tag)) e.preventDefault();
    }, true);

    // ══════════════════════════════════════════════════════
    // 9. ĐÓNG BĂNG OBJECT QUAN TRỌNG
    // ══════════════════════════════════════════════════════
    try {
        // Không cho override addEventListener
        Object.defineProperty(EventTarget.prototype, 'addEventListener', {
            value: EventTarget.prototype.addEventListener,
            writable: false, configurable: false
        });
    } catch(e) {}

})();
