var nmproy = document.getElementById('nmproy').value;
var valid_nmproy = '{{ valid_nmproy }}';

function ValidateForm() {

    if (nmproy != valid_nmproy) {
      alert("nmpro_incorrect valid_nmproy ");
      return false;
    }
  }