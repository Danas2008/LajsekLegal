(function () {
  var form = document.getElementById('booking-form');
  if (!form) return;

  var hiddenInput = document.getElementById('booking-slot');
  var selectedLabel = document.getElementById('booking-selected');
  var buttons = form.querySelectorAll('.booking-slot');
  var selectedPrefix = form.getAttribute('data-selected-prefix') || 'Selected time:';
  var selectAlert = form.getAttribute('data-select-alert') || 'Please choose a meeting time.';
  var atWord = form.getAttribute('data-at-word') || 'at';

  buttons.forEach(function (btn) {
    btn.addEventListener('click', function () {
      buttons.forEach(function (b) { b.classList.remove('is-selected'); });
      btn.classList.add('is-selected');
      hiddenInput.value = btn.getAttribute('data-slot');
      selectedLabel.style.display = 'block';
      selectedLabel.textContent = selectedPrefix + ' ' + btn.closest('.booking-day').querySelector('h3').textContent + ' ' + atWord + ' ' + btn.textContent.trim();
    });
  });

  form.addEventListener('submit', function (event) {
    if (!hiddenInput.value) {
      event.preventDefault();
      alert(selectAlert);
    }
  });
})();
