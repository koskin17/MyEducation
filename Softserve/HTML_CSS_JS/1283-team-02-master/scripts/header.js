const burger = document.querySelector(".header__burger");
const headerPosition = document.querySelector(".header__position");
const topBar = document.querySelector(".header__top-bar");
const navContainer = document.querySelector(".header__nav-container");
const social = document.querySelector(".social");
const navLinks = document.querySelectorAll(".nav__link");
const body = document.body;
const heroSection = document.querySelector(".header__hero");

function toggleMenu() {
    burger.classList.toggle("open");
    headerPosition.classList.toggle("header__position--active");
    topBar.classList.toggle("header__top-bar--active");
    navContainer.classList.toggle("header__nav-container--active");
    social.classList.toggle("social--active");
    if (burger.classList.contains("open")) {
        body.style.overflow = "hidden";
    } else {
        body.style.overflow = "";
    }
}

if (burger) {
    burger.addEventListener("click", toggleMenu);
}

navLinks.forEach((link) => {
    link.addEventListener("click", toggleMenu);
});

if (window.location.pathname.includes("product.html")) {
    if (heroSection) {
        heroSection.style.display = "none";
    }
    headerPosition.style.position = "relative";
} else if (window.location.pathname.includes("index.html")) {
    if (heroSection) {
        heroSection.style.display = "block";
    }
    headerPosition.style.position = "absolute";
}
