// const carousel = document.querySelector('.carousel');
// const items = document.querySelectorAll('.carousel__item');
// const childCarousel = carousel.children;
// function getSlidesPerView() {
//   const width = window.innerWidth;
//   if (width >= 992) return 4;
//   if (width >= 768) return 2;
//   return 1;
// }
// // const prevButton = document.querySelector('.carousel__button--previous');
// // const nextButton = document.querySelector('.carousel__button--next');

// let currentIndex = 0;

// function updateCarousel() {
//   carousel.style.transform = `translateX(-${currentIndex * 20}%)`;
// }

// nextButton.addEventListener('click', () => {
//   if (currentIndex < items.length - 1) {
//     currentIndex++;
//     updateCarousel();
//   }
// });

// prevButton.addEventListener('click', () => {
//   if (currentIndex > 0) {
//     currentIndex--;
//     updateCarousel();
//   }
// });