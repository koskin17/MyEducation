const cards = [
    `<div class="carousel__card">
        <h3 class="carousel__year">2016</h3>
        <h4 class="carousel__heading">First Milestone</h4>
        <p class="carousel__text">NextLevel launched its online store, featuring a handpicked selection of tech gadgets.</p>
    </div>`,
    
    `<div class="carousel__card">
        <h3 class="carousel__year">2017</h3>
        <h4 class="carousel__heading">Expanding the Range</h4>
        <p class="carousel__text">With growing customer demand, the store expanded its product categories.</p>
    </div>`,
    
    `<div class="carousel__card">
        <h3 class="carousel__year">2019</h3>
        <h4 class="carousel__heading">Brands Partnership</h4>
        <p class="carousel__text">Partnered with leading tech brands to offer an even wider range of high-quality products.</p>
    </div>`,
    
    `<div class="carousel__card">
        <h3 class="carousel__year">2022</h3>
        <h4 class="carousel__heading">Free Shipping</h4>
        <p class="carousel__text">We launched free delivery service for orders over $100, offering more value to clients.</p>
    </div>`,
    
    `<div class="carousel__card">
        <h3 class="carousel__year">2023</h3>
        <h4 class="carousel__heading">New Innovations</h4>
        <p class="carousel__text">We added AI-powered shopping assistants to help customers find the perfect tech solutions.</p>
    </div>`
];

let currentIndex = 0;

function renderCarousel() {
    const carouselTrack = document.querySelector('.carousel__track');
    carouselTrack.innerHTML = cards[currentIndex]; // Показуємо перший слайд

    if (window.matchMedia("(min-width: 768px)").matches) {
        const secondSlideIdx = (currentIndex + 1) % cards.length;
        carouselTrack.innerHTML += cards[secondSlideIdx]; // Показуємо другий слайд
    }
    
    if (window.matchMedia("(min-width: 1024px)").matches) {
        const thirdSlideIdx = (currentIndex + 2) % cards.length;
        carouselTrack.innerHTML += cards[thirdSlideIdx];
        const fourthSlideIdx = (currentIndex + 3) % cards.length;
        carouselTrack.innerHTML += cards[fourthSlideIdx]; // Показуємо третій слайд
    }
}

function nextSlide() {
    currentIndex = (currentIndex + 1) % cards.length;
    renderCarousel();
}

function prevSlide() {
    currentIndex = (currentIndex - 1 + cards.length) % cards.length;
    renderCarousel();
}

renderCarousel();

const nextButton = document.querySelector('.our-story__carousel-nav--next');
if (nextButton) nextButton.addEventListener('click', nextSlide);

const prevButton = document.querySelector('.our-story__carousel-nav--prev');
if (prevButton) prevButton.addEventListener('click', prevSlide);

window.addEventListener('resize', renderCarousel);
