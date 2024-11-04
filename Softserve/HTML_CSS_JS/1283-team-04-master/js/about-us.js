function init() {
    import("./burger.js");
    import("./about-us.in-store-services-carousel.js");
    import("./about-us.our-story-carousel.js");
  }
  
  const totalPartials = document.querySelectorAll(
    '[hx-trigger="load"], [data-hx-trigger="load"]'
  ).length;
  let loadedPartialsCount = 0;
  
  document.body.addEventListener("htmx:afterOnLoad", () => {
    loadedPartialsCount++;
    if (loadedPartialsCount === totalPartials) init();
  });
  