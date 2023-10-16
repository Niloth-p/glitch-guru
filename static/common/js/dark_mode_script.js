$(document).ready(function () {
  const isDarkMode = localStorage.getItem("darkMode") === "true";

  if (isDarkMode) {
    $("body").addClass("dark-mode");
    $("table").addClass("table-dark");
  }

  function toggleDarkMode() {
    $("body").toggleClass("dark-mode");
    localStorage.setItem("darkMode", $("body").hasClass("dark-mode"));

    $("table").toggleClass("table-dark", $("body").hasClass("dark-mode"));
  }

  $("#darkModeToggle").click(function () {
    toggleDarkMode();
  });

});
