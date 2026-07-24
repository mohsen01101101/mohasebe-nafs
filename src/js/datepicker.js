function initDatepickerSync() {
  const datepicker = document.querySelector("doran-datepicker");
  const dateInput = document.getElementById("new-date");

  if (!datepicker || !dateInput) return;

  let currentDate = datepicker
    .querySelector(".doran-datepicker__value")
    .textContent.trim();

  dateInput.value = currentDate;

  const observer = new MutationObserver(() => {
    const newDate = datepicker
      .querySelector(".doran-datepicker__value")
      .textContent.trim();

    if (newDate !== currentDate) {
      currentDate = newDate;

      dateInput.value = newDate;

      document.body.dispatchEvent(new Event("app:dateChanged"));
    }
  });

  observer.observe(datepicker, {
    childList: true,
    characterData: true,
    subtree: true,
  });
}

document.addEventListener("DOMContentLoaded", initDatepickerSync);
