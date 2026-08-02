function syncDatepickerTitle() {
  const datepicker = document.querySelector("doran-datepicker");
  const title = document.getElementById("homepage-title");

  if (!datepicker || !title) return;

  const today = datepicker
    .querySelector(".doran-datepicker__value")
    .textContent.trim();

  const updateTitle = () => {
    const dateText = datepicker
      .querySelector(".doran-datepicker__value")
      .textContent.trim();

    if (dateText === today) {
      title.textContent = "اعمال امروز";
      title.classList.remove("text-lg");
      title.classList.add("text-2xl");
    } else {
      title.textContent = `اعمال ${dateText}`;
      title.classList.remove("text-2xl");
      title.classList.add("text-lg");
    }
  };

  datepicker.addEventListener("change", updateTitle);
}

document.addEventListener("DOMContentLoaded", syncDatepickerTitle);
