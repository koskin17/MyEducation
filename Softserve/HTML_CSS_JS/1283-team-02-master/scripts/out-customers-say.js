const slides = [
    `<div> 
      <div class="clients-carousel__slide">
        <img
          src="./assets/images/customer-say/dean-williams.png"
          alt="Slide 1"
          class="clients-carousel__image"
        />
        <p><span class="clients-carousel__name">Dean Williams</span></p>
        <span class="clients-carousel__say">
          “I often listen to music, and for me, first of all, it is important
          that the headphones sit comfortably on my head. In the Basside
          store, I've found exactly what I needed at a very nice price. The
          customer service also works great, and these guys helped me with the
          choice.”
        </span>
        <p><span class="clients-carousel__date">December 15, 2024</span></p>
      </в>
    </div>`,
    `<div> <div class="clients-carousel__slide">
          <img
            src="./assets/images/customer-say/jessica-gordons.png"
            alt="Slide 2"
            class="clients-carousel__image"
          />
          <p><span class="clients-carousel__name">Jessica Gordons</span></p>
          <span class="clients-carousel__say">
            “I listen to music during my morning runs and used to use earbuds
            before, but now I decided to try headphones. To my surprise, it is
            really very convenient, the headphones do not fall off while
            running. I would also like to thank the Basside store for quality
            advice and fast delivery!”
          </span>
          <p><span class="clients-carousel__date">March 28, 2024</span></p>
        </div>
        </div>`
        ,
    `<div> <div class="clients-carousel__slide">
          <img
            src="./assets/images/customer-say/eric-smith.png"
            alt="Slide 3"
            class="clients-carousel__image"
          />
          <p><span class="clients-carousel__name">Eric Smith</span></p>
          <span class="clients-carousel__say">
            “My new wireless headphones by Sennheiser work up to 14 hours on a
            single charge, wow! I can listen to music, then participate in a
            Zoom call, and watch some videos during my working day, without the
            need to recharge the battery. Thanks to Basside for such
            high-quality and stylish headphones.”
          </span>
          <p><span class="clients-carousel__date">May 29, 2024</span></p>
        </div>
        </div>`
];

let currentSlideIdx = 0;

function renderCarousel() {
   const slideContainer = document.querySelector('.product-carousel__slides');
   slideContainer.innerHTML = slides[currentSlideIdx];
  
  
}

function nextSlide() {
    currentSlideIdx = currentSlideIdx + 1 >= slides.length ? 0 : currentSlideIdx + 1;
    renderCarousel();
}

function prevSlide() {
    currentSlideIdx = currentSlideIdx - 1 < 0 ? slides.length - 1 : currentSlideIdx - 1;
    renderCarousel();
}


renderCarousel();

const nextBtn = document.querySelector('.product-carousel__btn-next');
nextBtn.addEventListener('click', nextSlide);

const prevBtn = document.querySelector('.product-carousel__btn-prev');
prevBtn.addEventListener('click', prevSlide);

window.addEventListener('resize', renderCarousel);

