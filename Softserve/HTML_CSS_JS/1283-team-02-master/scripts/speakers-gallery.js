window.addEventListener('load', () => {
  const emblaNode = document.querySelector('.embla');
  const options = { loop: true }; // Cyclic scrolling
  const embla = EmblaCarousel(emblaNode, options);

  // Control buttons
  const prevButton = document.querySelector('.embla__prev');
  const nextButton = document.querySelector('.embla__next');

  prevButton.addEventListener('click', embla.scrollPrev);
  nextButton.addEventListener('click', embla.scrollNext);
});
