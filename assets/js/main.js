// CyberQunit — shared site interactivity (no dependencies)
document.addEventListener('DOMContentLoaded', function () {
  // Footer year
  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();

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

  // Contact/demo form: friendly confirmation (mailto fallback already wired via form action)
  document.querySelectorAll('form.contact-form, form.modal-form').forEach(function (form) {
    form.addEventListener('submit', function () {
      setTimeout(function () {
        window.alert('Thanks — your email client should have opened with your request pre-filled to Help@qunittech.com. If nothing opened, please email us directly or use the WhatsApp button.');
      }, 300);
    });
  });
});
