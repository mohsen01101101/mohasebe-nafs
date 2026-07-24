function syncDatepickers() {
  const datepickers = document.querySelectorAll("doran-datepicker");

  const firstDatepicker = datepickers[0];
  const secondDatepicker = datepickers[1];

  firstDatepicker.addEventListener("change", function () {
    secondDatepicker.value = firstDatepicker.value;
  });
}

document.addEventListener("DOMContentLoaded", syncDatepickers);
