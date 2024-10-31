function init() {
  import("./header.js");
  import("./product-tabs.js");
  import("./headphones.js");
  import("./out-customers-say.js");
  import("./special-offers.js");
  import("./index.speakers.carousel.js");
}

const totalPartials = document.querySelectorAll(
  '[hx-trigger="load"], [data-hx-trigger="load"]'
).length;
let loadedPartialsCount = 0;

document.body.addEventListener("htmx:afterOnLoad", () => {
  loadedPartialsCount++;
  if (loadedPartialsCount === totalPartials) init();
});
