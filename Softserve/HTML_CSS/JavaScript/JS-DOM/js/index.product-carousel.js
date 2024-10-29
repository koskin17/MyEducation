const slides = [
  '<div><img src="img/baby-yoda.svg" alt="Baby Yoda"></div>',
  '<div><img src="img/banana.svg" alt="Banana"></div>',
  '<div><img src="img/girl.svg" alt="Girl"></div>',
  '<div><img src="img/viking.svg" alt="Viking"></div>',
];

let currentSlideIdx = 0;

function renderCarousel() {
  const slideContainer = document.querySelector(".product-carousel__slides");
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
  currentSlideIdx =
    currentSlideIdx + 1 >= slides.length ? 0 : currentSlideIdx + 1;
  renderCarousel();
}

function prevSlide() {
  currentSlideIdx =
    currentSlideIdx - 1 < 0 ? slides.length - 1 : currentSlideIdx - 1;
  renderCarousel();
}

setInterval(nextSlide, 3000);
renderCarousel();

const nextBtn = document.querySelector(".product-carousel__btn-next");
nextBtn.addEventListener("click", nextSlide);

const prevBtn = document.querySelector(".product-carousel__btn-prev");
prevBtn.addEventListener("click", prevSlide);

window.addEventListener("resize", renderCarousel);

/// Так не робимо, бо затирає інші обробники! nextBtn.onclick = nextSlide;
