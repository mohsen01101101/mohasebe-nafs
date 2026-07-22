function initDoranDatepicker() {
  const doranDatePicker = document.querySelector("doran-datepicker");

  if (!doranDatePicker) return;

  let currentDate = doranDatePicker
    .querySelector(".doran-datepicker__value")
    .textContent.trim();

  new MutationObserver(() => {
    const newDate = doranDatePicker
      .querySelector(".doran-datepicker__value")
      .textContent.trim();

    if (newDate === currentDate) return;

    currentDate = newDate;

    fetch(`/web-api/lists?jalali_date=${newDate}`)
      .then((response) => response.text())
      .then((html) => {
        document.querySelector("#lists-container").innerHTML = html;
      });
  }).observe(doranDatePicker, {
    childList: true,
    characterData: true,
  });
}

document.addEventListener("DOMContentLoaded", initDoranDatepicker);
