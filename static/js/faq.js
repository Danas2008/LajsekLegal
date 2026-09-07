(function () {
  var cards = document.querySelectorAll('.faq-card');

  cards.forEach(function (card) {
    var question = card.querySelector('.faq-question');
    question.addEventListener('click', function () {
      var isOpen = card.classList.toggle('is-open');
      question.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
  });

  var search = document.getElementById('faq-search');
  var empty = document.getElementById('faq-empty');
  if (!search) return;

  search.addEventListener('input', function () {
    var term = search.value.trim().toLowerCase();
    var visibleCount = 0;

    cards.forEach(function (card) {
      var text = card.textContent.toLowerCase();
      var matches = text.indexOf(term) !== -1;
      card.style.display = matches ? '' : 'none';
      if (matches) visibleCount += 1;
    });

    if (empty) empty.style.display = visibleCount === 0 ? 'block' : 'none';
  });
})();
