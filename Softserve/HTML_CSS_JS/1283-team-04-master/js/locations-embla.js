document.addEventListener("DOMContentLoaded", function () {
    const checkEmbla = () => {
      const emblaNode = document.querySelector(".embla__viewport");
      const prevButton = document.querySelector(".embla__arrow-btn--left");
      const nextButton = document.querySelector(".embla__arrow-btn--right");

      if (emblaNode) {
        const options = { align: "start", loop: true };
        const emblaApi = EmblaCarousel(emblaNode, options);

        prevButton.addEventListener("click", () => emblaApi.scrollPrev());
        nextButton.addEventListener("click", () => emblaApi.scrollNext());
        
        console.log(emblaApi.slideNodes());
      } else {
        setTimeout(checkEmbla, 100); // Перевіряйте кожні 100 мс
      }
    };
    checkEmbla(); // Запускаємо перевірку
  });