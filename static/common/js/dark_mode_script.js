$(document).ready(function () {
  const isDarkMode = localStorage.getItem("darkMode") === "true";
  const themeIcon = $("#themeIcon");

  if (isDarkMode) {
    themeIcon.removeClass("fa-moon");
    themeIcon.addClass("fa-sun");
    $("body").addClass("dark-mode");
    $("table").addClass("table-dark");
  }

  function toggleDarkMode() {
    themeIcon.toggleClass("fa-moon fa-sun");

    $("body").toggleClass("dark-mode");
    localStorage.setItem("darkMode", $("body").hasClass("dark-mode"));

    $("table").toggleClass("table-dark", $("body").hasClass("dark-mode"));
  }

  $("#darkModeToggle").click(function () {
    toggleDarkMode();
  });

});
