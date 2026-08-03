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

    document.body.dispatchEvent(
      new CustomEvent("app:dateChanged", {
        detail: {
          date: event.detail.date,
          iso: event.detail.iso,
        },
      }),
    );
  });
}

document.addEventListener("DOMContentLoaded", initDatepicker);

function getSelectedDate() {
  const hiddenInput = document.querySelector('input[name="selected_date_iso"]');

  if (!hiddenInput || !hiddenInput.value) {
    return new Date().toISOString().split("T")[0];
  }

  return hiddenInput.value;
}

window.getSelectedDate = getSelectedDate;
