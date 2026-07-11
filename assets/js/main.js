// CyberQunit — shared site interactivity (no dependencies)
document.addEventListener('DOMContentLoaded', function () {
  // Footer year
  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();

  // Hero terminal typewriter (homepage only)
  var typed = document.getElementById('typed');
  if (typed && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var seq = [
      ['whoami', 'CyberQunit — offensive security'],
      ['./scan --target you', '0 breaches. shields up.'],
      ['run vapt --ai', 'securing the AI you build.']
    ];
    var i = 0;
    function typeCmd(cmd, done) {
      var n = 0;
      (function step() {
        typed.textContent = cmd.slice(0, n++);
        if (n <= cmd.length) setTimeout(step, 55); else done();
      })();
    }
    function cycle() {
      var c = seq[i % seq.length];
      typeCmd(c[0], function () {
        setTimeout(function () {
          typed.innerHTML = c[0] + ' <span style="color:#5c6b7a">&#8594;</span> <span style="color:#eaf3f0">' + c[1] + '</span>';
          i++;
          setTimeout(cycle, 2400);
        }, 450);
      });
    }
    cycle();
  } else if (typed) {
    typed.innerHTML = 'whoami <span style="color:#5c6b7a">&#8594;</span> <span style="color:#eaf3f0">CyberQunit — offensive security</span>';
  }

  // Hero live-scan terminal (homepage)
  var termBody = document.getElementById('termBody');
  if (termBody) {
    var reduceT = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var PROMPT = '<span style="color:#34d399">visitor@cyberqunit:~$</span> ';
    var steps = [
      { cmd: 'whoami' },
      { out: 'CyberQunit — offensive security', c: '#67e8f9' },
      { gap: 1 },
      { cmd: './run-audit --target app.acme.io --scope full' },
      { out: '[+] recon ............ 128 assets mapped', c: '#8ea3b5' },
      { out: '[+] web app .......... OWASP Top 10', c: '#8ea3b5' },
      { out: '[+] api .............. OWASP API Top 10', c: '#8ea3b5' },
      { out: '[+] cloud ............ AWS · Azure · GCP', c: '#8ea3b5' },
      { out: '[+] auth ............. session · MFA · IAM', c: '#8ea3b5' },
      { out: '[+] ai / llm ......... prompt-injection', c: '#8ea3b5' },
      { out: '[!] high ............. 5', c: '#fbbf24' },
      { out: '[!] critical ......... 2', c: '#ff6b6b' },
      { out: '[i] evidence attached · CVSS scored', c: '#8ea3b5' },
      { out: '[✓] retest ........... remediation verified', c: '#34d399' },
      { out: '[✓] report ........... delivered', c: '#34d399' },
      { gap: 1 },
      { cmd: 'status' },
      { out: 'shields up. 0 breaches.', c: '#67e8f9' }
    ];
    var htmlBuf = '';
    function renderT(active) {
      termBody.innerHTML = htmlBuf + (active || '') + '<span class="term-cursor"></span>';
      termBody.scrollTop = termBody.scrollHeight;
    }
    function typeCmd(txt, done) {
      if (reduceT) { htmlBuf += PROMPT + txt + '\n'; renderT(); return done(); }
      var n = 0;
      (function st() {
        renderT(PROMPT + txt.slice(0, n++));
        if (n <= txt.length) setTimeout(st, 45);
        else { htmlBuf += PROMPT + txt + '\n'; setTimeout(done, 380); }
      })();
    }
    function printOut(txt, c, done) {
      htmlBuf += '<span style="color:' + (c || '#dbe6f5') + '">' + txt + '</span>\n';
      renderT();
      setTimeout(done, reduceT ? 0 : 300);
    }
    (function runTerm() {
      var i = 0;
      (function next() {
        if (i >= steps.length) { setTimeout(function () { htmlBuf = ''; runTerm(); }, 2800); return; }
        var s = steps[i++];
        if (s.cmd) typeCmd(s.cmd, next);
        else if (s.out) printOut(s.out, s.c, next);
        else setTimeout(next, 320);
      })();
    })();
  }

  // Mobile nav toggle
  var toggle = document.getElementById('menuToggle');
  var navList = document.getElementById('navList');
  if (toggle && navList) {
    toggle.addEventListener('click', function () {
      var open = navList.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    // Tap-to-open submenu on touch/mobile
    navList.querySelectorAll('li.group > a').forEach(function (a) {
      a.addEventListener('click', function (e) {
        if (window.innerWidth <= 720) {
          e.preventDefault();
          a.closest('li').classList.toggle('mega-open');
        }
      });
    });
  }

  // Book demo modal
  var openBtn = document.getElementById('bookDemoBtn');
  var closeBtn = document.getElementById('closeBookDemo');
  var modal = document.getElementById('bookDemoModal');
  if (openBtn && modal) {
    openBtn.addEventListener('click', function () { modal.classList.remove('hidden'); });
  }
  if (closeBtn && modal) {
    closeBtn.addEventListener('click', function () { modal.classList.add('hidden'); });
  }
  if (modal) {
    modal.addEventListener('click', function (e) { if (e.target === modal) modal.classList.add('hidden'); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') modal.classList.add('hidden'); });
  }

  // FAQ / accordions
  document.querySelectorAll('.accordion-btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var item = btn.closest('.accordion-item');
      var wasOpen = item.classList.contains('open');
      item.parentElement.querySelectorAll('.accordion-item.open').forEach(function (i) {
        if (i !== item) i.classList.remove('open');
      });
      item.classList.toggle('open', !wasOpen);
    });
  });

  // Contact/demo form: submit to FormSubmit (emails Help@qunittech.com) via fetch,
  // show inline confirmation, no page reload. Falls back to mailto if the request fails.
  function showFormMsg(form, text, ok) {
    var m = form.querySelector('.form-status');
    if (!m) {
      m = document.createElement('p');
      m.className = 'form-status';
      form.appendChild(m);
    }
    m.textContent = text;
    m.style.cssText = 'margin-top:12px;font-size:.9rem;font-weight:600;padding:10px 14px;border-radius:9px;' +
      (ok ? 'color:#065f46;background:rgba(52,211,153,.15);border:1px solid rgba(52,211,153,.4);'
          : 'color:#7f1d1d;background:rgba(239,68,68,.12);border:1px solid rgba(239,68,68,.4);');
  }
  document.querySelectorAll('form.contact-form, form.modal-form').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var btn = form.querySelector('[type="submit"]');
      var orig = btn ? btn.textContent : '';
      if (btn) { btn.disabled = true; btn.textContent = 'Sending…'; }
      fetch(form.action, { method: 'POST', body: new FormData(form), headers: { 'Accept': 'application/json' } })
        .then(function (r) { if (!r.ok) throw new Error('bad'); return r.json(); })
        .then(function () {
          form.reset();
          showFormMsg(form, 'Thank you — your message has been sent. Our team will reply within one business day.', true);
        })
        .catch(function () {
          showFormMsg(form, 'Could not send just now. Please email Help@qunittech.com or use WhatsApp.', false);
        })
        .finally(function () { if (btn) { btn.disabled = false; btn.textContent = orig; } });
    });
  });
});
