/* Первым делом делаем для карусели новый, отдельный partial-файл: index.products-carousel.partial.html */
/* Создаём массив слайдов */
const slides = [
  /* Делаем слайды в виде строки, которая включает в себя div.
  Можно было бы не делать div, а сразу вставить картинки, то наличие div показывается, что внутри может быть сколько угодно и какого угодно кода html */
  '<div><img src="img/baby-yoda.svg" alt="Baby Yoda"></div>',
  '<div><img src="img/banana.svg" alt="Banana"></div>',
  '<div><img src="img/girl.svg" alt="Girl"></div>',
  '<div><img src="img/viking.svg" alt="Viking"></div>',
];

/* Создаём переменную для подсчёта индекса элементов карусели */
let currentSlideIndex = 0;

/* Дальше делаем функцию для карусели */
function renderCarousel() {
  const slideContainer = document.querySelector(".product-carousel__slides");
  /* Дальше в контейнер product-carousel__slides в innerHtml вставляется из массива slides элемент, который соответствует индексу currentSlideIndex */
  slideContainer.innerHTML = slides[currentSlideIndex];
  /* Добавляем проверку ширина окна и в зависимости от этого отображаем определенное кол-во слайдов */
  if (window.matchMedia("(min-width: 768px)").matches) {
    const secondSlideIndex =
      currentSlideIndex + 1 >= slides.length ? 0 : currentSlideIndex + 1;
    slideContainer.innerHTML += slides[secondSlideIndex];
    if (window.matchMedia("(min-width: 1024px)").matches) {
      const thirdSlideIndex =
        secondSlideIndex + 1 >= slides.length ? 0 : secondSlideIndex + 1;
      slideContainer.innerHTML += slides[thirdSlideIndex];
    }
  }
}

/* Теперь нужно сделать так, чтобы добавлялся следующий слайд */
function nextSlide() {
  /* Увеличиваем индекс текущего слайда на 1 */
  currentSlideIndex++;
  /* Если currentSlideIndex выходит за пределы массива, т.е. кол-ва элементов в массиве, то мы его сбрасываем на ноль */
  if (currentSlideIndex >= slides.length) currentSlideIndex = 0;
  /* Также это можно записать в один ряд:
  currentSlideIndex = currentSlideIndex + 1 >= slides.length ? 0 : currentSlideIndex + 1; */
  /* и вызываем функцию renderCarousel */
  renderCarousel();
}

/* Функция для отображения предыдущего слайда */
function prevSlide() {
  currentSlideIndex =
    currentSlideIndex - 1 < 0 ? slides.length - 1 : currentSlideIndex - 1;
  renderCarousel();
}

/* Также можно сделать автоматический показ слайдов через 3 секунды */
setInterval(nextSlide, 3000);
/* Также нужно обязательно отрисовать слайды первый раз. Иначе в течение 3 ервых секунд будет пустое место на странице.
Для этого просто вызываем функию renderCarousel() */
renderCarousel();

/* Делаем рабочими кнопки */
const nextBtn = document.querySelector(".product-carousel__btn-next");
nextBtn.addEventListener("click", nextSlide);

const prevBtn = document.querySelector(".product-carousel__btn-prev");
prevBtn.addEventListener("click", prevSlide);

/* Для того, чтобы галерея перерисовывалась сама при любом изменении размера окна нужно добавить: */
window.addEventListener("resize", renderCarousel);

/* Главный минус этой карусели в том, что она меняет innerHtml, а у него нет анимации */
