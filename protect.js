// ==========================================
// protect.js  –  Bảo vệ chống DevTools / F12
// FIX: Không ghi đè window.fetch trực tiếp (TypeError read-only)
// ==========================================

(function () {
  'use strict';

  // ─── CẢNH BÁO CONSOLE ───────────────────────────────────────────────
  var s1 = 'background:#1a1a2e;color:#ff4444;font-size:18px;font-weight:bold;padding:10px 20px;border-left:4px solid #ff4444;';
  var s2 = 'background:#1a1a2e;color:#ffaa00;font-size:13px;padding:5px 20px;';
  console.log('%c ⚠️  CẢNH BÁO BẢO MẬT ', s1);
  console.log('%c Khu vực này được theo dõi và bảo vệ. ', s2);
  console.log('%c Mọi hành động can thiệp đều bị ghi lại và báo cáo quản trị viên. ', s2);
  console.log('%c Liên hệ hỗ trợ: t.me/sewdangcap ', s2);

  // ─── CHẶN CHUỘT PHẢI ────────────────────────────────────────────────
  document.addEventListener('contextmenu', function (e) {
    e.preventDefault();
    return false;
  });

  // ─── CHẶN PHÍM TẮT DEV ──────────────────────────────────────────────
  document.addEventListener('keydown', function (e) {
    if (e.keyCode === 123) { e.preventDefault(); return false; }
    if (e.ctrlKey && e.shiftKey && (e.keyCode === 73 || e.keyCode === 74 || e.keyCode === 67)) {
      e.preventDefault(); return false;
    }
    if (e.ctrlKey && e.keyCode === 85) { e.preventDefault(); return false; }
  });

  // ─── PHÁT HIỆN DEVTOOLS (size-based) ────────────────────────────────
  var _devtoolsOpen = false;

  function _isDevToolsOpen() {
    var threshold = 160;
    return (
      window.outerWidth  - window.innerWidth  > threshold ||
      window.outerHeight - window.innerHeight > threshold
    );
  }

  function _sendSecurityAlert(reason) {
    try {
      var username = (document.body && document.body.getAttribute('data-user')) || null;
      // FIX: Gọi fetch bình thường - KHÔNG ghi đè window.fetch
      fetch('/api/security-alert', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ reason: reason || 'devtools_detected', user: username })
      }).catch(function () {});
    } catch (e) {}
  }

  setInterval(function () {
    if (_isDevToolsOpen()) {
      if (!_devtoolsOpen) {
        _devtoolsOpen = true;
        _sendSecurityAlert('devtools_detected');
      }
    } else {
      _devtoolsOpen = false;
    }
  }, 2000);

  // ─── OBSERVER: chặn script injection từ ngoài ───────────────────────
  // FIX: KHÔNG ghi đè window.fetch trong observer, chỉ xóa script lạ
  try {
    var _observer = new MutationObserver(function (mutations) {
      try {
        mutations.forEach(function (mutation) {
          mutation.addedNodes.forEach(function (node) {
            if (!node || node.tagName !== 'SCRIPT') return;
            var src = node.src || '';
            if (!src) return;
            var hostname = window.location.hostname;
            var isLocal   = src.indexOf(hostname) !== -1 ||
                            src.indexOf('localhost') !== -1 ||
                            src.indexOf('127.0.0.1') !== -1;
            var isTrusted = src.indexOf('cdnjs.cloudflare.com') !== -1 ||
                            src.indexOf('cdn.jsdelivr.net') !== -1 ||
                            src.indexOf('ajax.googleapis.com') !== -1;
            if (!isLocal && !isTrusted) {
              try { node.parentNode.removeChild(node); } catch (_) {}
            }
          });
        });
      } catch (_) {}
    });
    _observer.observe(document.documentElement, { childList: true, subtree: true });
  } catch (e) {}

})();
