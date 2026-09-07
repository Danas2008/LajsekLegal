(function () {
  var form = document.getElementById('booking-form');
  if (!form) return;

  var hiddenInput = document.getElementById('booking-slot');
  var selectedLabel = document.getElementById('booking-selected');
  var buttons = form.querySelectorAll('.booking-slot');

  buttons.forEach(function (btn) {
    btn.addEventListener('click', function () {
      buttons.forEach(function (b) { b.classList.remove('is-selected'); });
      btn.classList.add('is-selected');
      hiddenInput.value = btn.getAttribute('data-slot');
      selectedLabel.style.display = 'block';
      selectedLabel.textContent = 'Vybraný termín: ' + btn.closest('.booking-day').querySelector('h3').textContent + ' v ' + btn.textContent.trim();
    });
  });

  form.addEventListener('submit', function (event) {
    if (!hiddenInput.value) {
      event.preventDefault();
      alert('Vyberte prosím termín schůzky.');
    }
  });
})();
