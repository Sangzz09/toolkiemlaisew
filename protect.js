;(function(){
'use strict';

// ── Lưu native trước khi bị override ─────────────────────────────────────
var _nat={};
['log','warn','error','info','debug','clear','table','dir'].forEach(function(m){
  try{_nat[m]=console[m].bind(console);}catch(e){}
});
var _origFetch   = window.fetch ? window.fetch.bind(window) : null;
var _origST      = window.setTimeout.bind(window);
var _origSI      = window.setInterval.bind(window);
var _origXHR     = window.XMLHttpRequest;
var _dead        = false;
var _warned      = false;
var _csrfCache   = null;
var _csrfExp     = 0;
var _TTL         = 240000;

// ══════════════════════════════════════════════════════════════
// 1. PHÍM TẮT + CHUỘT PHẢI
// ══════════════════════════════════════════════════════════════
function _killKey(e){
  var c=e.ctrlKey||e.metaKey,s=e.shiftKey,k=e.key||'';
  if(k==='F12'||(c&&!s&&'uUsSpP'.indexOf(k)>-1)||(c&&s&&'iIjJcCkK'.indexOf(k)>-1)){
    e.preventDefault();e.stopPropagation();e.stopImmediatePropagation();
    return false;
  }
}
window.addEventListener('keydown',_killKey,true);
document.addEventListener('keydown',_killKey,true);
document.addEventListener('contextmenu',function(e){
  e.preventDefault();e.stopImmediatePropagation();return false;
},true);

// ══════════════════════════════════════════════════════════════
// 2. DỪNG TOOL - gọi khi phát hiện tấn công
// ══════════════════════════════════════════════════════════════
function _nuke(){
  if(_dead)return; _dead=true;

  // Dừng tất cả interval/timeout
  try{
    var hid=_origST(function(){},0);
    for(var i=0;i<=hid+100;i++){try{clearInterval(i);clearTimeout(i);}catch(e){}}
  }catch(e){}

  // Kill fetch + XHR
  var _blk=function(){return Promise.reject(new Error('x'));};
  try{Object.defineProperty(window,'fetch',{value:_blk,writable:false,configurable:false});}
  catch(e){window.fetch=_blk;}
  window.apiFetch=_blk;
  try{
    window.XMLHttpRequest=function(){
      this.open=this.send=this.setRequestHeader=function(){};
      this.readyState=4;this.status=403;
      this.onload=this.onerror=null;
    };
  }catch(e){}

  // Gọi server logout ngay lập tức
  try{
    var img=new Image();
    img.src='/logout?reason=devtools&t='+Date.now();
  }catch(e){}

  // Hiện thông báo
  try{document.documentElement.innerHTML='';}catch(e){}
  document.open();
  document.write('<style>*{margin:0;padding:0;background:#0a1628;box-sizing:border-box}</style>'+
    '<div style="display:flex;height:100vh;align-items:center;justify-content:center;'+
    'flex-direction:column;gap:16px;font-family:Arial,sans-serif;color:#fff;text-align:center;padding:20px">'+
    '<div style="font-size:64px">🛑</div>'+
    '<div style="font-size:22px;font-weight:bold;color:#ff4444">Phát hiện công cụ tấn công!</div>'+
    '<div style="font-size:14px;color:#aaa;max-width:340px">Hành động của bạn đã bị ghi lại và báo cáo admin.<br>Phiên đã bị hủy.</div>'+
    '<button onclick="location.href=\'/logout\'" '+
    'style="margin-top:12px;padding:12px 28px;background:#00e6b4;border:none;border-radius:10px;'+
    'color:#0a1628;font-size:15px;font-weight:bold;cursor:pointer">Đăng nhập lại</button></div>');
  document.close();
}

// ══════════════════════════════════════════════════════════════
// 3. KHÓA CONSOLE + CHẶN CODE CHẠY
// ══════════════════════════════════════════════════════════════
(function lockConsole(){
  // Hiện cảnh báo 1 lần
  try{
    _nat.warn('%c CÓ TRÌNH ĐÉO MÀ LẤY','color:#f00;font-size:28px;font-weight:900;background:#000;padding:8px 16px');
    _nat.warn('%c Mua key: t.me/sewdangcap','color:#f80;font-size:15px;font-weight:bold');
    _nat.warn('%c MOI CODE PASTE/CHAY O DAY DEU BI CHAN & BAO CAO ADMIN','color:#ff4444;font-size:13px');
  }catch(e){}

  var _noop=function(){return undefined;};
  var ms=['log','warn','error','info','debug','table','dir','dirxml',
          'group','groupCollapsed','groupEnd','time','timeEnd','timeLog',
          'trace','clear','count','countReset','assert','profile','profileEnd'];
  ms.forEach(function(m){
    try{
      Object.defineProperty(console,m,{
        get:function(){return _noop;},set:function(){},
        configurable:false,enumerable:false
      });
    }catch(e){try{console[m]=_noop;}catch(x){}}
  });

  // Chặn eval
  try{
    Object.defineProperty(window,'eval',{
      get:function(){_nuke();return function(){throw new Error('blocked');};},
      set:function(){},configurable:false
    });
  }catch(e){}

  // Chặn Function constructor
  try{
    Object.defineProperty(window,'Function',{
      get:function(){return function(){throw new Error('blocked');};},
      set:function(){},configurable:false
    });
  }catch(e){}

  // Chặn setTimeout/setInterval với string code
  window.setTimeout=function(fn,d){
    if(typeof fn==='string'){_nuke();return 0;}
    return _origST.apply(window,arguments);
  };
  window.setInterval=function(fn,d){
    if(typeof fn==='string'){_nuke();return 0;}
    return _origSI.apply(window,arguments);
  };

  // ── CHẶN EXTENSION / BOOKMARKLET INJECT SCRIPT ─────────────────────────
  // Theo dõi MutationObserver - phát hiện script tag mới được inject
  try{
    var _mo=new MutationObserver(function(mutations){
      mutations.forEach(function(m){
        m.addedNodes.forEach(function(node){
          if(node.tagName==='SCRIPT'&&!node.src){
            // Script inline mới được thêm vào DOM → xóa ngay
            try{node.parentNode.removeChild(node);}catch(e){}
            _nuke();
          }
        });
      });
    });
    _mo.observe(document.documentElement,{childList:true,subtree:true});
  }catch(e){}

  // Chặn document.write từ bên ngoài (extension dùng document.write để inject)
  var _origWrite=document.write.bind(document);
  try{
    var _writeCount=0;
    Object.defineProperty(document,'write',{
      get:function(){
        return function(s){
          // Cho phép _nuke() dùng document.write
          if(_dead){return _origWrite(s);}
          // Chặn script injection
          if(s&&/<script/i.test(s)){_nuke();return;}
          _origWrite(s);
        };
      },
      set:function(){},configurable:false
    });
  }catch(e){}

})();

// ══════════════════════════════════════════════════════════════
// 4. PHÁT HIỆN DEVTOOLS - 4 phương pháp
// ══════════════════════════════════════════════════════════════
// A: debugger timing
function _chkDbg(){
  var t=performance.now();
  (function(){debugger;})();
  if(performance.now()-t>80)_nuke();
}
// B: console object getter
var _spy={_v:false};
Object.defineProperty(_spy,'_v',{get:function(){_nuke();return false;}});
function _chkConsole(){
  try{_nat.log&&_nat.log(_spy);_nat.clear&&_nat.clear();}catch(e){}
}
// C: size diff
function _chkSize(){
  if(window.outerWidth-window.innerWidth>200||
     window.outerHeight-window.innerHeight>200)_nuke();
}
_origSI(_chkDbg,    1000);
_origSI(_chkConsole,1500);
_origSI(_chkSize,    800);

// ══════════════════════════════════════════════════════════════
// 5. PHÁT HIỆN EXTENSION INJECT (Web Analyzer, v4.0, etc.)
// ══════════════════════════════════════════════════════════════
(function detectExtension(){
  // Theo dõi thay đổi bất thường trong DOM (extension thêm element lạ)
  var _knownIds = ['predictionPopup','gameFrame','fullscreenIframe',
                   'particles-js','robotAvatar'];

  _origSI(function(){
    // Kiểm tra có element lạ không thuộc template
    var allEls = document.querySelectorAll('[id]');
    for(var i=0;i<allEls.length;i++){
      var id = allEls[i].id;
      if(id && _knownIds.indexOf(id)<0 &&
         /analyzer|extractor|inject|crack|tool|hack/i.test(id)){
        _nuke(); return;
      }
    }
    // Kiểm tra có div overlay lạ không (tool thường tạo overlay)
    var overlays = document.querySelectorAll('div[style*="position: fixed"]');
    for(var j=0;j<overlays.length;j++){
      var el = overlays[j];
      var txt = (el.textContent||'').toLowerCase();
      if(/analyzer|extractor|web.*pro|download|extract/i.test(txt)){
        el.remove();
        _nuke(); return;
      }
    }
  }, 500);
})();

// ══════════════════════════════════════════════════════════════
// 6. CSRF TOKEN - TỰ ĐỘNG GẮN VÀO MỌI FETCH
// ══════════════════════════════════════════════════════════════
async function _getToken(){
  var now=Date.now();
  if(_csrfCache&&now<_csrfExp)return _csrfCache;
  try{
    var r=await _origFetch('/api/csrf-token',{credentials:'same-origin'});
    var j=await r.json();
    if(j.ok){_csrfCache=j.token;_csrfExp=now+_TTL;return _csrfCache;}
  }catch(e){}
  return null;
}
var _safeFetch=async function(url,opts){
  opts=Object.assign({},opts||{},{credentials:'same-origin'});
  if(typeof url==='string'&&url.startsWith('/api/')&&url.indexOf('csrf-token')<0){
    var tk=await _getToken();
    if(tk){var h=new Headers(opts.headers||{});h.set('X-CSRF-Token',tk);opts.headers=h;}
  }
  return _origFetch(url,opts);
};
try{
  Object.defineProperty(window,'fetch',{value:_safeFetch,writable:false,configurable:false});
}catch(e){window.fetch=_safeFetch;}
window.apiFetch=_safeFetch;

// ══════════════════════════════════════════════════════════════
// 7. CHẶN PASTE CODE + CHỌN TEXT + IN TRANG
// ══════════════════════════════════════════════════════════════
document.addEventListener('paste',function(e){
  var tag=((e.target||{}).tagName||'').toUpperCase();
  if(tag==='INPUT'||tag==='TEXTAREA'||tag==='SELECT')return;
  e.preventDefault();e.stopImmediatePropagation();
  try{
    var txt=(e.clipboardData||window.clipboardData).getData('text')||'';
    var bad=[/fetch\s*\(/i,/XMLHttp/i,/eval\s*\(/i,/\.cookie/i,
             /localStorage/i,/Function\s*\(/i,/atob\s*\(/i,/import\s*\(/i,/<script/i];
    if(bad.some(function(r){return r.test(txt);})){
      _nuke();
    }
  }catch(x){}
  return false;
},true);

document.addEventListener('selectstart',function(e){
  var tag=((e.target||{}).tagName||'').toUpperCase();
  if(tag!=='INPUT'&&tag!=='TEXTAREA')e.preventDefault();
},true);

window.addEventListener('beforeprint',function(){document.body.style.display='none';});
window.addEventListener('afterprint', function(){document.body.style.display='';});

// ══════════════════════════════════════════════════════════════
// 8. ĐÓNG BĂNG API QUAN TRỌNG
// ══════════════════════════════════════════════════════════════
try{
  Object.defineProperty(document,'cookie',{
    get:function(){return '';},set:function(){},configurable:false
  });
}catch(e){}

// Chặn đọc HTML source qua JS
try{
  var _origGEBI = document.getElementById.bind(document);
  // Không cho clone toàn bộ document
  Object.defineProperty(document,'documentElement',{
    get:function(){return document.querySelector('html');},
    configurable:false
  });
}catch(e){}

// ══════════════════════════════════════════════════════════════
// 9. ANTI-TAMPER: phát hiện script bị inject sau khi load
// ══════════════════════════════════════════════════════════════
// Theo dõi window object - extension thường gắn biến vào window
var _winKeys = Object.keys(window).length;
_origSI(function(){
  var newKeys = Object.keys(window).length;
  // Nếu có quá nhiều biến mới được inject (extension thường inject 10+ biến)
  if(newKeys > _winKeys + 15){
    _winKeys = newKeys; // reset để không nuke liên tục
    // Kiểm tra có biến tên nghi ngờ không
    var suspicious = Object.keys(window).filter(function(k){
      return /analyzer|extractor|injector|cracker|__ext|webext/i.test(k);
    });
    if(suspicious.length > 0) _nuke();
  }
}, 2000);

})();
