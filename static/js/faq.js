(function () {
  var items = document.querySelectorAll('.faq-item');

  items.forEach(function (item) {
    var question = item.querySelector('.faq-question');
    question.addEventListener('click', function () {
      item.classList.toggle('is-open');
    });
  });

  var search = document.getElementById('faq-search');
  var empty = document.getElementById('faq-empty');
  if (!search) return;

  search.addEventListener('input', function () {
    var term = search.value.trim().toLowerCase();
    var visibleCount = 0;

    items.forEach(function (item) {
      var text = item.textContent.toLowerCase();
      var matches = text.indexOf(term) !== -1;
      item.style.display = matches ? '' : 'none';
      if (matches) visibleCount += 1;
    });

    if (empty) empty.style.display = visibleCount === 0 ? 'block' : 'none';
  });
})();
