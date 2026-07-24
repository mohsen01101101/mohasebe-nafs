function syncDatepickerTitle() {
  const datepicker = document.querySelectorAll("doran-datepicker")[1];
  const title = document.getElementById("homepage-title");
  const today = datepicker
    .querySelector(".doran-datepicker__value")
    .textContent.trim();

  if (!datepicker || !title) return;

  const observer = new MutationObserver(() => {
    const dateText = datepicker
      .querySelector(".doran-datepicker__value")
      .textContent.trim();

    if (dateText == today) {
      title.textContent = `اعمال امروز`;
      title.classList.remove("text-lg");
      title.classList.add("text-2xl");
    } else {
      title.textContent = `اعمال ${dateText}`;
      title.classList.remove("text-2xl");
      title.classList.add("text-lg");
    }
  });

  observer.observe(datepicker, {
    childList: true,
    subtree: true,
  });
}

document.addEventListener("DOMContentLoaded", syncDatepickerTitle);
