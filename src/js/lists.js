function refreshLists() {
  document.body.dispatchEvent(new Event("lists:changed"));
}

window.refreshLists = refreshLists;
