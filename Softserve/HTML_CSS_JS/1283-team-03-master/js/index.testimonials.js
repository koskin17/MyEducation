document.addEventListener("DOMContentLoaded", () => {
  const carousel = document.querySelector('.testimonials__carousel');
  const testimonials = document.querySelectorAll('.testimonial');

  if (!carousel || testimonials.length === 0) {
    console.error('Carousel element or testimonials not found');
    return;
  }

  const prevButton = document.createElement('button');
  const nextButton = document.createElement('button');
  let currentIndex = 0;

  prevButton.innerHTML = '&#10094;';
  nextButton.innerHTML = '&#10095;';
  prevButton.className = 'carousel-prev';
  nextButton.className = 'carousel-next';

  carousel.appendChild(prevButton);
  carousel.appendChild(nextButton);

  function showTestimonial(index) {
    carousel.style.transform = `translateX(-${index * 100}%)`;
  }

  prevButton.addEventListener('click', () => {
    currentIndex = (currentIndex > 0) ? currentIndex - 1 : testimonials.length - 1;
    showTestimonial(currentIndex);
  });

  nextButton.addEventListener('click', () => {
    currentIndex = (currentIndex < testimonials.length - 1) ? currentIndex + 1 : 0;
    showTestimonial(currentIndex);
  });

  showTestimonial(currentIndex);
});
