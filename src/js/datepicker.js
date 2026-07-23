import { loadListActions } from "./lists.js";

function initDatepicker() {
  const datepicker = document.querySelector("doran-datepicker");

  if (!datepicker) return;

  const container = document.querySelector("#lists-container");

  let currentDate = datepicker
    .querySelector(".doran-datepicker__value")
    .textContent.trim();

  loadListActions(container, currentDate);

  const observer = new MutationObserver(() => {
    const newDate = datepicker
      .querySelector(".doran-datepicker__value")
      .textContent.trim();

    if (newDate !== currentDate) {
      currentDate = newDate;

      fetch(`/web-api/lists?jalali_date=${newDate}`)
        .then((response) => response.text())
        .then(async (html) => {
          container.innerHTML = html;
          await loadListActions(container, newDate);
        });
    }
  });

  observer.observe(datepicker, {
    childList: true,
    characterData: true,
    subtree: true,
  });
}

document.addEventListener("DOMContentLoaded", initDatepicker);
