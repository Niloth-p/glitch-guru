function handleLoadingError(libname) {
  alert(`Error loading ${libname}. Please try again later.`);
}

// Load Bootstrap CSS asynchronously
$.getScript(
  "https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
).fail(function () {
  handleLoadingError("bootstrap css");
});

// Load jQuery asynchronously
$.getScript(
  "https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"
).fail(function () {
  handleLoadingError("jquery");
});

// Load Popper.js asynchronously
$.getScript(
  "https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"
).fail(function () {
  handleLoadingError("popper");
});

// Load Bootstrap.js asynchronously
$.getScript(
  "https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"
).fail(function () {
  handleLoadingError("bootstrap js");
});
