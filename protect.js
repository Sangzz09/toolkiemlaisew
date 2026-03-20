// ================== protect.js ==================
// Chặn F12, Ctrl+U, chuột phải, DevTools
// Copy file này vào project, nhúng vào tất cả trang HTML:
// <script src="/static/protect.js"></script>

(function () {
    'use strict';

    // ── 1. Chặn chuột phải ──────────────────────────────────────────────
    document.addEventListener('contextmenu', function (e) {
        e.preventDefault();
        return false;
    });

    // ── 2. Chặn phím tắt nguy hiểm ──────────────────────────────────────
    document.addEventListener('keydown', function (e) {
        const key = e.key;
        const ctrl = e.ctrlKey || e.metaKey;
        const shift = e.shiftKey;

        // F12 - Mở DevTools
        if (key === 'F12') { e.preventDefault(); return false; }

        // Ctrl+U - Xem nguồn trang
        if (ctrl && key.toLowerCase() === 'u') { e.preventDefault(); return false; }

        // Ctrl+Shift+I - DevTools
        if (ctrl && shift && key.toLowerCase() === 'i') { e.preventDefault(); return false; }

        // Ctrl+Shift+J - Console
        if (ctrl && shift && key.toLowerCase() === 'j') { e.preventDefault(); return false; }

        // Ctrl+Shift+C - Inspect element
        if (ctrl && shift && key.toLowerCase() === 'c') { e.preventDefault(); return false; }

        // Ctrl+Shift+K - Console Firefox
        if (ctrl && shift && key.toLowerCase() === 'k') { e.preventDefault(); return false; }

        // Ctrl+S - Lưu trang
        if (ctrl && key.toLowerCase() === 's') { e.preventDefault(); return false; }

        // Ctrl+A - Chọn tất cả (tùy chọn, bỏ comment nếu muốn)
        // if (ctrl && key.toLowerCase() === 'a') { e.preventDefault(); return false; }
    });

    // ── 3. Phát hiện DevTools đang mở → chuyển hướng ────────────────────
    var devtoolsOpen = false;
    var threshold = 160;

    function checkDevTools() {
        var widthDiff  = window.outerWidth  - window.innerWidth;
        var heightDiff = window.outerHeight - window.innerHeight;

        if (widthDiff > threshold || heightDiff > threshold) {
            if (!devtoolsOpen) {
                devtoolsOpen = true;
                onDevToolsDetected();
            }
        } else {
            devtoolsOpen = false;
        }
    }

    function onDevToolsDetected() {
        // Xóa toàn bộ nội dung trang
        document.documentElement.innerHTML =
            '<div style="display:flex;align-items:center;justify-content:center;' +
            'height:100vh;background:#0a1628;color:#ff4444;font-size:28px;' +
            'font-family:sans-serif;text-align:center;flex-direction:column;gap:20px;">' +
            '<div style="font-size:60px;">🚫</div>' +
            '<div>Không được sử dụng DevTools!</div>' +
            '<div style="font-size:16px;color:#888;">Vui lòng đóng Developer Tools và tải lại trang.</div>' +
            '<button onclick="location.reload()" ' +
            'style="margin-top:20px;padding:12px 30px;background:#00e6b4;border:none;' +
            'border-radius:10px;color:#0a1628;font-size:16px;font-weight:bold;cursor:pointer;">' +
            '🔄 Tải lại trang</button>' +
            '</div>';
    }

    // Kiểm tra liên tục mỗi 1 giây
    setInterval(checkDevTools, 1000);

    // ── 4. Chặn kéo thả chọn văn bản (bảo vệ nội dung) ─────────────────
    document.addEventListener('selectstart', function (e) {
        // Chỉ chặn bên ngoài input/textarea
        var tag = e.target.tagName.toLowerCase();
        if (tag !== 'input' && tag !== 'textarea') {
            e.preventDefault();
        }
    });

    // ── 5. Vô hiệu hóa in trang ─────────────────────────────────────────
    window.addEventListener('beforeprint', function () {
        document.body.style.display = 'none';
    });
    window.addEventListener('afterprint', function () {
        document.body.style.display = '';
    });

})();

// ── 6. Chặn Self-XSS / Console injection ────────────────────────────────────
(function blockConsole() {
    // Ghi đè toàn bộ console
    var noop = function () {};
    var warnOnce = false;

    var handler = {
        get: function (target, prop) {
            if (typeof target[prop] === 'function') {
                return function () {
                    if (!warnOnce) {
                        warnOnce = true;
                        // Ghi thông báo cảnh báo duy nhất bằng native log
                        target['warn'].call(target,
                            '%c⛔ CẢNH BÁO BẢO MẬT!',
                            'color:red;font-size:24px;font-weight:bold;'
                        );
                        target['warn'].call(target,
                            '%cNếu ai đó bảo bạn paste code vào đây, đó là lừa đảo!\nHọ đang cố chiếm tài khoản của bạn.',
                            'color:orange;font-size:14px;'
                        );
                    }
                };
            }
            return target[prop];
        }
    };

    try {
        // Ghi đè console bằng Proxy
        window.console = new Proxy(console, handler);
    } catch (e) {
        // Fallback: ghi đè thủ công từng method
        ['log','warn','error','info','debug','table','dir','group','groupEnd','time','timeEnd','trace','clear','count','assert'].forEach(function(m) {
            try { window.console[m] = noop; } catch(ex) {}
        });
    }
})();

// ── 7. Phát hiện paste code vào trang (Self-XSS protection) ─────────────────
document.addEventListener('paste', function (e) {
    var target = e.target;
    var tag = target ? target.tagName.toLowerCase() : '';

    // Chỉ cho phép paste vào input/textarea bình thường
    if (tag !== 'input' && tag !== 'textarea') {
        e.preventDefault();

        // Kiểm tra nếu clipboard có chứa code JS
        try {
            var text = (e.clipboardData || window.clipboardData).getData('text');
            var jsPatterns = [
                /fetch\s*\(/i,
                /XMLHttpRequest/i,
                /eval\s*\(/i,
                /document\.cookie/i,
                /localStorage/i,
                /sessionStorage/i,
                /window\.location/i,
                /<script/i,
                /javascript:/i,
                /atob\s*\(/i,
                /btoa\s*\(/i,
                /Function\s*\(/i,
            ];
            var isCode = jsPatterns.some(function(p) { return p.test(text); });
            if (isCode) {
                alert('⛔ Không được phép!\n\nBạn đang cố paste code độc hại.\nHành động này đã được ghi lại.');
            }
        } catch (ex) {}

        return false;
    }
});

// ── 8. Chống dùng debugger / breakpoint ─────────────────────────────────────
setInterval(function () {
    var start = new Date();
    // eslint-disable-next-line no-debugger
    debugger;
    var end = new Date();
    // Nếu debugger bị dừng lại > 100ms → đang bị debug
    if (end - start > 100) {
        document.documentElement.innerHTML =
            '<div style="display:flex;align-items:center;justify-content:center;' +
            'height:100vh;background:#0a1628;color:#ff4444;font-size:24px;' +
            'font-family:sans-serif;text-align:center;flex-direction:column;gap:16px;">' +
            '<div style="font-size:56px;">🚫</div>' +
            '<div>Phát hiện công cụ hack!</div>' +
            '<div style="font-size:14px;color:#888;">Phiên đăng nhập đã bị hủy.</div>' +
            '</div>';
        // Logout phiên
        setTimeout(function() { window.location.href = '/logout'; }, 2000);
    }
}, 3000);
