const checkCarousel = () => {
  const carouselNode = document.querySelector(".embla__viewport");
  const slidesContainer = document.querySelector(".embla__container");
  const slides = Array.from(document.querySelectorAll(".embla__slide"));
  const prevButton = document.querySelector(".embla__arrow-btn--left");
  const nextButton = document.querySelector(".embla__arrow-btn--right");

  if (carouselNode && slidesContainer && slides.length > 1) {
    const repeatCount = 10;

    for (let i = 0; i < repeatCount; i++) {
      const startClones = slides.map((slide) => slide.cloneNode(true));
      const endClones = slides.map((slide) => slide.cloneNode(true)).reverse();

      endClones.forEach((clone) =>
        slidesContainer.insertBefore(clone, slidesContainer.firstChild),
      );
      startClones.forEach((clone) => slidesContainer.appendChild(clone));
    }

    const options = { align: "start", loop: false };
    const emblaApi = EmblaCarousel(carouselNode, options);

    emblaApi.on("init", () => {
      emblaApi.scrollTo(slides.length * repeatCount, false);
    });

    prevButton.addEventListener("click", () => emblaApi.scrollPrev());
    nextButton.addEventListener("click", () => emblaApi.scrollNext());

    console.log(emblaApi.slideNodes());
  } else {
    setTimeout(checkCarousel, 100);
  }
};
checkCarousel();

const countdownContainers = document.querySelectorAll(".product-card__timer");

const currentYear = new Date().getFullYear();

const border1FinalDate = new Date(`February 25, ${currentYear + 1} 00:00:00`);
const border2FinalDate = new Date(`March 15, ${currentYear + 1} 15:00:00`);
const border3FinalDate = new Date(`May 28, ${currentYear + 1} 08:00:00`);

function updateCountdown() {
  const currentTime = new Date();
  
  const diffBorder1 = border1FinalDate - currentTime;
  const diffBorder2 = border2FinalDate - currentTime;
  const diffBorder3 = border3FinalDate - currentTime;
  
  const daysLeftBorder1 = Math.floor(diffBorder1 / 1000 / 60 / 60 / 24);
  const hoursLeftBorder1 = Math.floor(diffBorder1 / 1000 / 60 / 60) % 24;
  const minutesLeftBorder1 = Math.floor(diffBorder1 / 1000 / 60) % 60;

  const daysLeftBorder2 = Math.floor(diffBorder2 / 1000 / 60 / 60 / 24);
  const hoursLeftBorder2 = Math.floor(diffBorder2 / 1000 / 60 / 60) % 24;
  const minutesLeftBorder2 = Math.floor(diffBorder2 / 1000 / 60) % 60;

  const daysLeftBorder3 = Math.floor(diffBorder3 / 1000 / 60 / 60 / 24);
  const hoursLeftBorder3 = Math.floor(diffBorder3 / 1000 / 60 / 60) % 24;
  const minutesLeftBorder3 = Math.floor(diffBorder3 / 1000 / 60) % 60;

  countdownContainers.forEach((container, index) => {
    switch(index) {
      case 0:
        container.querySelector(".timer__days").innerText = daysLeftBorder1;
        container.querySelector(".timer__hours").innerText = hoursLeftBorder1;
        container.querySelector(".timer__minutes").innerText = minutesLeftBorder1;
        break;
      case 1:
        container.querySelector(".timer__days").innerText = daysLeftBorder2;
        container.querySelector(".timer__hours").innerText = hoursLeftBorder2;
        container.querySelector(".timer__minutes").innerText = minutesLeftBorder2;
        break;
      case 2:
        container.querySelector(".timer__days").innerText = daysLeftBorder3;
        container.querySelector(".timer__hours").innerText = hoursLeftBorder3;
        container.querySelector(".timer__minutes").innerText = minutesLeftBorder3;
        break;
    }
  });
}
setInterval(updateCountdown, 1000);