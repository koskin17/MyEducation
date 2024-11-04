const slides = [
  `<div class="in-store-services__slider-list__item">
    <div class="in-store-services__slider-list__item-img">
      <img src="images/product-demos.webp" alt="Product Demos" />
      <h2 class="in-store-services__slider-list__item-title">Product Demos</h2>
      <p class="in-store-services__slider-list__item-description">
        Experience live demonstrations of the latest tech. Test out products
        firsthand to see how they fit into your lifestyle.
      </p>
    </div>
  </div>`,

  `<div class="in-store-services__slider-list__item">
    <div class="in-store-services__slider-list__item-img">
      <img src="images/setup-and-installation.webp" alt="Setup and Installation" />
      <h2 class="in-store-services__slider-list__item-title">Setup and Installation</h2>
      <p class="in-store-services__slider-list__item-description">
        Let our team handle the setup and installation of your new devices,
        so you can start using them right away, hassle-free.
      </p>
    </div>
  </div>`,

  `<div class="in-store-services__slider-list__item">
    <div class="in-store-services__slider-list__item-img">
      <img src="images/product-consultations.webp" alt="Product Consultations" />
      <h2 class="in-store-services__slider-list__item-title">Product Consultations</h2>
      <p class="in-store-services__slider-list__item-description">
        Get tailored advice from NextLevel experts to help you choose the
        right tech products based on your needs and preferences.
      </p>
    </div>
  </div>`,

  `<div class="in-store-services__slider-list__item">
    <div class="in-store-services__slider-list__item-img">
      <img src="images/repair-and-maintenance.webp" alt="Repair and Maintenance" />
      <h2 class="in-store-services__slider-list__item-title">Repair and Maintenance</h2>
      <p class="in-store-services__slider-list__item-description">
        Our skilled technicians are available to troubleshoot, repair, and
        maintain your devices, ensuring they perform at their best.
      </p>
    </div>
  </div>`,
];

let currentSlideIdx = 0;

function renderCarousel() {
  const slideContainer = document.querySelector(
    ".in-store-services__slider-slides"
  );
  slideContainer.innerHTML = slides[currentSlideIdx];
  if (window.matchMedia("(min-width: 768px)").matches) {
    const secondSlideIdx =
      currentSlideIdx + 1 >= slides.length ? 0 : currentSlideIdx + 1;
    slideContainer.innerHTML += slides[secondSlideIdx];
    if (window.matchMedia("(min-width: 1024px)").matches) {
      const thirdSlideIdx =
        secondSlideIdx + 1 >= slides.length ? 0 : secondSlideIdx + 1;
      slideContainer.innerHTML += slides[thirdSlideIdx];
    }
  }
}

function nextSlide() {
  currentSlideIdx = (currentSlideIdx + 1) % slides.length;
  renderCarousel();
}

function prevSlide() {
  currentSlideIdx = (currentSlideIdx - 1 + slides.length) % slides.length;
  renderCarousel();
}

// setInterval(nextSlide, 5000);
renderCarousel();

const nextBtn = document.querySelector(".in-store-services__slider__btn-prev");
if (nextBtn) nextBtn.addEventListener("click", nextSlide);

const prevBtn = document.querySelector(".in-store-services__slider__btn-next");
if (prevBtn) prevBtn.addEventListener("click", prevSlide);

window.addEventListener("resize", renderCarousel);
