function initDatepicker() {
  const datepicker = document.querySelector("doran-datepicker");

  if (!datepicker) return;

  datepicker.addEventListener("change", (event) => {
    const hiddenInput = document.querySelector(
      'input[name="selected_date_iso"]',
    );

    if (hiddenInput) {
      hiddenInput.value = event.detail.iso;
    }

    document.body.dispatchEvent(new CustomEvent("app:dateChanged"));
  });
}

document.addEventListener("DOMContentLoaded", initDatepicker);
