const slides = [
  '<div class="testimonials__slider-item">' +
    '<div class="testimonials__slider-item-quotes">' +
      '<img src="images/quotes.svg" alt="Slider Quotes" />' +
    '</div>' +
    '<p class="testimonials__slider-item-name">Emily Rosewood</p>' +
    '<p class="testimonials__slider-item-text">' +
      '“I love shopping at NextLevel. Their customer support helped me ' +
      'choose the perfect monitor, and the entire process was hassle-free ' +
      'from start to finish. Delivery was quick, the packaging was secure, ' +
      'and the prices are super competitive. I’ve never had such a smooth ' +
      'online shopping experience!”' +
    '</p>' +
    '<p class="testimonials__slider-item-date">September 24, 2024</p>' +
  '</div>',

  '<div class="testimonials__slider-item">' +
    '<div class="testimonials__slider-item-quotes">' +
      '<img src="images/quotes.svg" alt="Slider Quotes" />' +
    '</div>' +
    '<p class="testimonials__slider-item-name">David Linderman</p>' +
    '<p class="testimonials__slider-item-text">' +
      '“Great service and top-quality products. I found everything I needed, ' +
      'and the checkout was smooth and secure. The detailed product ' +
      'descriptions made choosing the right gadgets a breeze, and the fast ' +
      'shipping was a huge bonus. It’s clear that customer satisfaction is ' +
      'a priority at NextLevel.”' +
    '</p>' +
    '<p class="testimonials__slider-item-date">August 02, 2024</p>' +
  '</div>',

  '<div class="testimonials__slider-item">' +
    '<div class="testimonials__slider-item-quotes">' +
      '<img src="images/quotes.svg" alt="Slider Quotes" />' +
    '</div>' +
    '<p class="testimonials__slider-item-name">Sarah Peterson</p>' +
    '<p class="testimonials__slider-item-text">' +
      '“NextLevel is my go-to for tech! The selection is amazing, and my ' +
      'order arrived super fast. The product quality exceeded my ' +
      'expectations, and I was impressed by how easy it was to navigate the ' +
      'site. I’ve recommended it to friends, and I’ll definitely be ' +
      'shopping here again.”' +
    '</p>' +
    '<p class="testimonials__slider-item-date">June 15, 2024</p>' +
  '</div>'
];

let currentSlideIdx = 0;

function renderCarousel() {
  const slideContainer = document.querySelector('.testimonials__slider-slides');
  if (slideContainer) {
    slideContainer.innerHTML = slides[currentSlideIdx];
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

setInterval(nextSlide, 5000);
renderCarousel();

const nextBtn = document.querySelector('.testimonials__slider__btn-prev');
if (nextBtn) nextBtn.addEventListener('click', nextSlide);

const prevBtn = document.querySelector('.testimonials__slider__btn-next');
if (prevBtn) prevBtn.addEventListener('click', prevSlide);

window.addEventListener('resize', renderCarousel);
