(function () {
  document.querySelectorAll('[data-newsletter-form]').forEach(function (form) {
    var message = form.parentElement.querySelector('.newsletter-message');

    form.addEventListener('submit', function (event) {
      event.preventDefault();

      fetch(form.getAttribute('action'), {
        method: 'POST',
        body: new FormData(form),
      })
        .then(function (response) { return response.json(); })
        .then(function (data) {
          if (data.ok) {
            form.hidden = true;
            if (message) {
              message.textContent = data.message;
              message.hidden = false;
            }
          } else if (message) {
            message.textContent = 'Zadejte prosím platný e-mail.';
            message.hidden = false;
          }
        })
        .catch(function () {
          if (message) {
            message.textContent = 'Něco se pokazilo, zkuste to prosím později.';
            message.hidden = false;
          }
        });
    });
  });
})();
