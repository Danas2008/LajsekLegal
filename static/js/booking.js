(function () {
  var form = document.getElementById('booking-form');
  var calendar = document.getElementById('booking-calendar');
  if (!form || !calendar) return;

  var slotsByDate = JSON.parse(calendar.getAttribute('data-slots') || '{}');
  var lang = calendar.getAttribute('data-lang') || 'cs';

  var hiddenInput = document.getElementById('booking-slot');
  var selectedLabel = document.getElementById('booking-selected');
  var selectedPrefix = form.getAttribute('data-selected-prefix') || 'Selected time:';
  var selectAlert = form.getAttribute('data-select-alert') || 'Please choose a meeting time.';
  var atWord = form.getAttribute('data-at-word') || 'at';
  var pickDayText = form.getAttribute('data-pick-day') || 'First, choose a day';
  var noSlotsDayText = form.getAttribute('data-no-slots-day') || 'No available time on this day.';

  var MONTHS = {
    cs: ['leden', 'únor', 'březen', 'duben', 'květen', 'červen', 'červenec', 'srpen', 'září', 'říjen', 'listopad', 'prosinec'],
    en: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
  };
  var WEEKDAYS = {
    cs: ['Po', 'Út', 'St', 'Čt', 'Pá', 'So', 'Ne'],
    en: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
  };
  var WEEKDAYS_LONG = {
    cs: ['pondělí', 'úterý', 'středa', 'čtvrtek', 'pátek', 'sobota', 'neděle'],
    en: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
  };

  function isoDate(date) {
    return date.getFullYear() + '-' + String(date.getMonth() + 1).padStart(2, '0') + '-' + String(date.getDate()).padStart(2, '0');
  }

  var availableDates = Object.keys(slotsByDate).sort();
  if (availableDates.length === 0) return;

  var minDate = new Date(availableDates[0] + 'T00:00:00');
  var maxDate = new Date(availableDates[availableDates.length - 1] + 'T00:00:00');

  var viewYear = minDate.getFullYear();
  var viewMonth = minDate.getMonth();
  var selectedDate = null;

  var monthLabel = document.getElementById('cal-month-label');
  var weekdaysEl = document.getElementById('cal-weekdays');
  var daysEl = document.getElementById('cal-days');
  var prevBtn = document.getElementById('cal-prev');
  var nextBtn = document.getElementById('cal-next');
  var timePanelTitle = document.getElementById('time-panel-title');
  var timeSlotsEl = document.getElementById('time-slots');

  function renderWeekdayHeader() {
    weekdaysEl.innerHTML = '';
    WEEKDAYS[lang].forEach(function (label) {
      var el = document.createElement('span');
      el.textContent = label;
      weekdaysEl.appendChild(el);
    });
  }

  function canGoPrev() {
    var firstOfView = new Date(viewYear, viewMonth, 1);
    return firstOfView > new Date(minDate.getFullYear(), minDate.getMonth(), 1);
  }

  function canGoNext() {
    var firstOfView = new Date(viewYear, viewMonth, 1);
    return firstOfView < new Date(maxDate.getFullYear(), maxDate.getMonth(), 1);
  }

  function renderCalendar() {
    monthLabel.textContent = MONTHS[lang][viewMonth] + ' ' + viewYear;
    prevBtn.disabled = !canGoPrev();
    nextBtn.disabled = !canGoNext();

    daysEl.innerHTML = '';

    var firstOfMonth = new Date(viewYear, viewMonth, 1);
    var startWeekday = (firstOfMonth.getDay() + 6) % 7; // Monday = 0
    var daysInMonth = new Date(viewYear, viewMonth + 1, 0).getDate();

    for (var i = 0; i < startWeekday; i++) {
      daysEl.appendChild(document.createElement('span'));
    }

    for (var day = 1; day <= daysInMonth; day++) {
      var date = new Date(viewYear, viewMonth, day);
      var iso = isoDate(date);
      var hasSlots = !!slotsByDate[iso] && slotsByDate[iso].length > 0;

      var btn = document.createElement('button');
      btn.type = 'button';
      btn.textContent = String(day);
      btn.className = 'cal-day' + (hasSlots ? ' has-slots' : ' disabled');
      if (iso === selectedDate) btn.classList.add('is-selected');

      if (hasSlots) {
        btn.addEventListener('click', function (clickedIso) {
          return function () {
            selectedDate = clickedIso;
            renderCalendar();
            renderTimeSlots();
          };
        }(iso));
      } else {
        btn.disabled = true;
      }

      daysEl.appendChild(btn);
    }
  }

  function renderTimeSlots() {
    timeSlotsEl.innerHTML = '';

    if (!selectedDate) {
      timePanelTitle.textContent = pickDayText;
      return;
    }

    var dateObj = new Date(selectedDate + 'T00:00:00');
    var weekdayName = WEEKDAYS_LONG[lang][(dateObj.getDay() + 6) % 7];
    var label = weekdayName.charAt(0).toUpperCase() + weekdayName.slice(1) + ' ' + dateObj.getDate() + '. ' + (dateObj.getMonth() + 1) + '. ' + dateObj.getFullYear();
    timePanelTitle.textContent = label;

    var slots = slotsByDate[selectedDate] || [];
    if (slots.length === 0) {
      var empty = document.createElement('p');
      empty.textContent = noSlotsDayText;
      timeSlotsEl.appendChild(empty);
      return;
    }

    slots.forEach(function (isoSlot) {
      var slotDate = new Date(isoSlot);
      var hh = String(slotDate.getHours()).padStart(2, '0');
      var mm = String(slotDate.getMinutes()).padStart(2, '0');

      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'booking-slot';
      btn.textContent = hh + ':' + mm;
      if (isoSlot === hiddenInput.value) btn.classList.add('is-selected');

      btn.addEventListener('click', function () {
        timeSlotsEl.querySelectorAll('.booking-slot').forEach(function (b) { b.classList.remove('is-selected'); });
        btn.classList.add('is-selected');
        hiddenInput.value = isoSlot;
        selectedLabel.style.display = 'block';
        selectedLabel.textContent = selectedPrefix + ' ' + label + ' ' + atWord + ' ' + hh + ':' + mm;
      });

      timeSlotsEl.appendChild(btn);
    });
  }

  prevBtn.addEventListener('click', function () {
    if (!canGoPrev()) return;
    viewMonth -= 1;
    if (viewMonth < 0) { viewMonth = 11; viewYear -= 1; }
    renderCalendar();
  });

  nextBtn.addEventListener('click', function () {
    if (!canGoNext()) return;
    viewMonth += 1;
    if (viewMonth > 11) { viewMonth = 0; viewYear += 1; }
    renderCalendar();
  });

  renderWeekdayHeader();
  renderCalendar();
  renderTimeSlots();

  form.addEventListener('submit', function (event) {
    if (!hiddenInput.value) {
      event.preventDefault();
      alert(selectAlert);
    }
  });
})();
