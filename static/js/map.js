(function () {
  var facade = document.getElementById('map-facade');
  var wrap = document.getElementById('map-embed');
  var iframe = document.getElementById('map-iframe');
  if (!facade || !wrap || !iframe) return;

  facade.addEventListener('click', function () {
    iframe.src = iframe.getAttribute('data-src');
    wrap.classList.add('is-loaded');
  });
})();
