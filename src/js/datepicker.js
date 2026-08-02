function initDatepicker() {
  const datepicker = document.querySelector("doran-datepicker");

  if (!datepicker) return;

  datepicker.addEventListener("change", (event) => {
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
  const datepicker = document.querySelector("doran-datepicker");

  if (!datepicker || !datepicker.value) {
    return new Date().toISOString().split("T")[0];
  }

  return datepicker.value.epochMs
    ? new Date(datepicker.value.epochMs).toLocaleDateString("en-CA", {
        timeZone: "Asia/Tehran",
      })
    : null;
}
window.getSelectedDate = getSelectedDate;
