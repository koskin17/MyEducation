/* Create a list of slides */

const slides = [
  '<article class="speakers__card">\
        <a href="product.html" class="link-to-product-page" data-id="jbl_br-55"><img class="speakers__card-image" src="assets/images/speakers_pics/jbl_br-55.png" alt="Speaker model JBL BR-55">\
        <p class="speakers__card-title"><a href="product.html" class="link-to-product-page" data-id="jbl_br-55">JBL BR-55</a></p>\
        <p class="speakers__card-price">$140.00</p>\
        <a class="speakers__card-link" href="#">ADD TO CART</a>\
    </article>',
  '<article class="speakers__card">\
        <a href="product.html" class="link-to-product-page" data-id="jbl_gt-345"><img class="speakers__card-image" src="assets/images/speakers_pics/jbl_gt-345.png" alt="Speaker model JBL GT-345">\
        <p class="speakers__card-title"><a href="product.html" class="link-to-product-page" data-id="jbl_gt-345">JBL GT-345</a></p>\
        <p class="speakers__card-price">$120.00</p>\
        <a class="speakers__card-link" href="#">ADD TO CART</a>\
    </article>',
  '<article class="speakers__card">\
        <a href="product.html" class="link-to-product-page" data-id="jbl_or-57"><img class="speakers__card-image" src="assets/images/speakers_pics/jbl_or-57.png" alt="Speaker model JBL OR-57">\
        <p class="speakers__card-title"><a href="product.html" class="link-to-product-page" data-id="jbl_or-57">JBL OR-57</a></p>\
        <p class="speakers__card-price">$98.00</p>\
        <a class="speakers__card-link" href="#">ADD TO CART</a>\
    </article>',
  '<article class="speakers__card">\
        <a href="product.html" class="link-to-product-page" data-id="jbl_party_pt-25"><img class="speakers__card-image" src="assets/images/speakers_pics/jbl_party_pt-25.png" alt="Speaker model JBL Party PT-25">\
        <p class="speakers__card-title"><a href="product.html" class="link-to-product-page" data-id="jbl_party_pt-25">JBL Party PT-25</a></p>\
        <p class="speakers__card-price">$180.00</p>\
        <a class="speakers__card-link" href="#">ADD TO CART</a>\
    </article>',
  '<article class="speakers__card">\
        <a href="product.html" class="link-to-product-page" data-id="jbl_rr-56"><img class="speakers__card-image" src="assets/images/speakers_pics/jbl_rr-56.png" alt="Speaker model JBL RR-56">\
        <p class="speakers__card-title"><a href="product.html" class="link-to-product-page" data-id="jbl_rr-56">JBL RR-56</a></p>\
        <p class="speakers__card-price">$110.00</p>\
        <a class="speakers__card-link" href="#">ADD TO CART</a>\
    </article>',
  '<article class="speakers__card">\
        <a href="product.html" class="link-to-product-page" data-id="sony_yt555"><img class="speakers__card-image" src="assets/images/speakers_pics/sony_yt555.png" alt="Speaker model Sony YT555">\
        <p class="speakers__card-title"><a href="product.html" class="link-to-product-page" data-id="sony_yt555">Sony YT555</a></p>\
        <p class="speakers__card-price">$140.00</p>\
        <a class="speakers__card-link" href="#">ADD TO CART</a>\
    </article>',
];

/* Create a variable for the index of carousel elements */
let currentSlideIndex = 0;

/* The function of the carousel of the columns */
function renderCarousel() {
  const slideContainer = document.querySelector(".speakers-carousel__slides");
  slideContainer.innerHTML = slides[currentSlideIndex];

  if (window.matchMedia("(min-width: 768px)").matches) {
    const secondSlideIndex =
      currentSlideIndex + 1 >= slides.length ? 0 : currentSlideIndex + 1;
    slideContainer.innerHTML += slides[secondSlideIndex];

    if (window.matchMedia("(min-width: 1024px)").matches) {
      const thirdSlideIndex =
        secondSlideIndex + 1 >= slides.length ? 0 : secondSlideIndex + 1;
      slideContainer.innerHTML += slides[thirdSlideIndex];

      const fourthSlideIndex =
        thirdSlideIndex + 1 >= slides.length ? 0 : thirdSlideIndex + 1;
      slideContainer.innerHTML += slides[fourthSlideIndex];

      const fifthSlideIndex =
        fourthSlideIndex + 1 >= slides.length ? 0 : fourthSlideIndex + 1;
      slideContainer.innerHTML += slides[fifthSlideIndex];
    }
  }
}

/* Function for the next slide */
function nextSlide() {
  currentSlideIndex++;
  if (currentSlideIndex >= slides.length) currentSlideIndex = 0;
  renderCarousel();
}

/* Function for displaying the previous slide */
function prevSlide() {
  currentSlideIndex =
    currentSlideIndex - 1 < 0 ? slides.length - 1 : currentSlideIndex - 1;
  renderCarousel();
}

renderCarousel();

/* Gallery scroll buttons */
const nextBtn = document.querySelector(".speakers-carousel__btn-next");
nextBtn.addEventListener("click", nextSlide);
const prevBtn = document.querySelector(".speakers-carousel__btn-prev");
prevBtn.addEventListener("click", prevSlide);

window.addEventListener("resize", renderCarousel);
