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
    link.addEventListener("click", (event) => {
        const targetSection = link.getAttribute("href");

        if (window.location.pathname.includes("product.html")) {
            event.preventDefault();
            if (window.innerWidth <= 990) {
                toggleMenu();
                setTimeout(() => {
                    body.style.overflow = "";
                    window.location.href = `index.html${targetSection}`;
                }, 300);
            } else {
                window.location.href = `index.html${targetSection}`;
            }
        } else {
            if (window.innerWidth <= 990) {
                event.preventDefault();
                toggleMenu();
                const targetElement = document.querySelector(targetSection);
                if (targetElement) {
                    setTimeout(() => {
                        targetElement.scrollIntoView({ behavior: "smooth" });
                    }, 300);
                }
            } else {
                event.preventDefault();
                const targetElement = document.querySelector(targetSection);
                if (targetElement) {
                    targetElement.scrollIntoView({ behavior: "smooth" });
                }
            }
        }
    });
});

function updateHeroSection() {
    if (window.location.pathname.includes("product.html")) {
        if (heroSection) {
            heroSection.style.display = "none";
        }
        headerPosition.style.position = "relative";
    } else {
        if (heroSection) {
            heroSection.style.display = "flex";
        }
        headerPosition.style.position = "absolute";

        const hash = window.location.hash;
        if (hash) {
            setTimeout(() => {
                const targetElement = document.querySelector(hash);
                if (targetElement) {
                    targetElement.scrollIntoView({ behavior: "smooth" });
                }
            }, 100);
        }
    }
}

window.addEventListener("load", updateHeroSection);

window.addEventListener("popstate", updateHeroSection);
window.addEventListener("hashchange", updateHeroSection);
