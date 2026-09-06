(function () {
  var toggle = document.querySelector('.js-toggle-edit');
  if (!toggle) return;

  var editables = document.querySelectorAll('.editable');

  function getCookie(name) {
    var match = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
    return match ? match.pop() : '';
  }

  function setEditMode(on) {
    document.body.classList.toggle('site-edit-on', on);
    editables.forEach(function (el) {
      el.setAttribute('contenteditable', on ? 'true' : 'false');
    });
    toggle.setAttribute('aria-pressed', on ? 'true' : 'false');
  }

  toggle.addEventListener('click', function () {
    var isOn = document.body.classList.contains('site-edit-on');
    setEditMode(!isOn);
  });

  editables.forEach(function (el) {
    el.addEventListener('blur', function () {
      if (!document.body.classList.contains('site-edit-on')) return;
      var key = el.getAttribute('data-edit-key');
      fetch('/LegalDashboard/api/text/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({ key: key, content: el.innerHTML.trim() }),
      });
    });
  });

  setEditMode(false);
})();
