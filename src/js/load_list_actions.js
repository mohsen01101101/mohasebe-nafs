export async function loadListActions(root, date) {
  const containers = root.querySelectorAll("[data-actions-url]");

  for (const container of containers) {
    const url = container.dataset.actionsUrl;

    const response = await fetch(`${url}?jalali_date=${date}`);

    if (response.ok) {
      const html = await response.text();
      container.innerHTML = html;
    } else {
      container.innerHTML = "خطا در بارگذاری اعمال";
    }
  }
}
