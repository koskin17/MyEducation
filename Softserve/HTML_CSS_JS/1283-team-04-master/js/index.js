function init() {
  import("./burger.js");
  import("./category.js");
  import("./promotion-cards-timer.js");
  import("./index.testimonials-carousel.js");
  import("./global.cart.js");
}

const totalPartials = document.querySelectorAll(
  '[hx-trigger="load"], [data-hx-trigger="load"]'
).length;
let loadedPartialsCount = 0;

document.body.addEventListener("htmx:afterOnLoad", () => {
  loadedPartialsCount++;
  if (loadedPartialsCount === totalPartials) init();
});
