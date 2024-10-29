function init() {
  import("./index.header-text.js");
  import("./index.header-clock.js"); /* файл JS для часов в меню */
  import("./index.product-list.js");
  import("./index.product-carusel.js");
  import("./index.product-animated-carusel.js");
  import("./index.faq-accordion.js");
}

const totalPartials = document.querySelectorAll(
  '[hx-trigger="load"], [data-hx-trigger="load"]'
).length;
let loadedPartialsCount = 0;

document.body.addEventListener("htmx:afterOnLoad", () => {
  loadedPartialsCount++;
  if (loadedPartialsCount === totalPartials) init();
});
