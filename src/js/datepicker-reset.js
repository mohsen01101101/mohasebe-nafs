function resetDoranForm(form) {
  form.reset();

  const dp = form.querySelector("doran-datepicker");
  if (dp) dp.value = null;

  const hiddenInput = form.querySelector('input[name="selected_date_iso"]');
  if (hiddenInput) hiddenInput.value = "";
}

document.body.addEventListener("htmx:afterRequest", (event) => {
  if (event.detail.successful) {
    const form = event.detail.elt;

    if (
      form &&
      form.tagName === "FORM" &&
      form.querySelector("doran-datepicker")
    ) {
      resetDoranForm(form);
    }
  }
});
