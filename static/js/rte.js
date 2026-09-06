(function () {
  function initEditor(wrap) {
    var toolbar = wrap.querySelector('.rte-toolbar');
    var editor = wrap.querySelector('.rte-editor');
    var textarea = wrap.nextElementSibling;
    if (!textarea || textarea.tagName !== 'TEXTAREA') return;

    textarea.style.display = 'none';
    editor.innerHTML = textarea.value;

    function sync() {
      textarea.value = editor.innerHTML;
    }

    editor.addEventListener('input', sync);

    toolbar.querySelectorAll('[data-cmd]').forEach(function (control) {
      var cmd = control.getAttribute('data-cmd');

      if (control.tagName === 'SELECT') {
        control.addEventListener('change', function () {
          if (!control.value) return;
          editor.focus();
          document.execCommand(cmd, false, control.value);
          sync();
          control.value = '';
        });
      } else {
        control.addEventListener('click', function () {
          editor.focus();
          document.execCommand(cmd, false, null);
          sync();
        });
      }
    });

    var form = wrap.closest('form');
    if (form) {
      form.addEventListener('submit', sync);
    }
  }

  document.querySelectorAll('.rte-wrap').forEach(initEditor);
})();
