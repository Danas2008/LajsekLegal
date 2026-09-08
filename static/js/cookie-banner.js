(function () {
  var STORAGE_KEY = 'cookie_consent';
  var CONSENT_DAYS = 180;

  var TEXT = {
    cs: {
      message: 'Tento web používá cookies pro zajištění základní funkčnosti a (se souhlasem) pro analýzu návštěvnosti. Více v <a href="/osobni-udaje/">Osobní údaje</a>.',
      accept: 'Přijmout vše',
      essential: 'Pouze nezbytné',
    },
    en: {
      message: 'This website uses cookies for core functionality and, with your consent, to analyse traffic. More in <a href="/osobni-udaje/">Privacy</a>.',
      accept: 'Accept all',
      essential: 'Essential only',
    },
  };

  var lang = (document.documentElement.getAttribute('lang') || 'cs').indexOf('en') === 0 ? 'en' : 'cs';
  var t = TEXT[lang];

  function readConsent() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return null;
      var data = JSON.parse(raw);
      if (!data.expires || Date.now() > data.expires) return null;
      return data.value;
    } catch (e) {
      return null;
    }
  }

  function writeConsent(value) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify({
        value: value,
        expires: Date.now() + CONSENT_DAYS * 24 * 60 * 60 * 1000,
      }));
    } catch (e) { /* localStorage unavailable, consent just won't persist */ }
  }

  function loadAnalytics() {
    var id = window.GA_MEASUREMENT_ID;
    if (!id || document.getElementById('ga-gtag-script')) return;

    var script = document.createElement('script');
    script.id = 'ga-gtag-script';
    script.async = true;
    script.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(id);
    document.head.appendChild(script);

    window.dataLayer = window.dataLayer || [];
    window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };
    gtag('js', new Date());
    gtag('config', id);
  }

  function applyConsent(value) {
    if (value === 'all') loadAnalytics();
  }

  var existing = readConsent();
  if (existing) {
    applyConsent(existing);
    return;
  }

  var banner = document.createElement('div');
  banner.className = 'cookie-banner';
  banner.setAttribute('role', 'dialog');
  banner.setAttribute('aria-label', 'Cookies');
  banner.innerHTML =
    '<p class="cookie-banner-text">' + t.message + '</p>' +
    '<div class="cookie-banner-actions">' +
      '<button type="button" class="cookie-btn cookie-btn-secondary" data-consent="essential">' + t.essential + '</button>' +
      '<button type="button" class="cookie-btn cookie-btn-primary" data-consent="all">' + t.accept + '</button>' +
    '</div>';

  document.body.appendChild(banner);
  window.requestAnimationFrame(function () {
    banner.classList.add('is-visible');
  });

  banner.addEventListener('click', function (event) {
    var button = event.target.closest('[data-consent]');
    if (!button) return;
    var value = button.getAttribute('data-consent');
    writeConsent(value);
    applyConsent(value);
    banner.classList.remove('is-visible');
    window.setTimeout(function () { banner.remove(); }, 250);
  });
})();
