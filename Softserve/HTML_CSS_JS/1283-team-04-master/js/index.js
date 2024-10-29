function init() {
  import("./burger.js");
  import("./category.js");
  import("./category-filters.js");
  import("./promotion-cards-timer.js");
  import("./index.testimonials-carousel.js");
}

const totalPartials = document.querySelectorAll(
  '[hx-trigger="load"], [data-hx-trigger="load"]'
).length;
let loadedPartialsCount = 0;

document.body.addEventListener("htmx:afterOnLoad", () => {
  loadedPartialsCount++;
  if (loadedPartialsCount === totalPartials) init();
});
