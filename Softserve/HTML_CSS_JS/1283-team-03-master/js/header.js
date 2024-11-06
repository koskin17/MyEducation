const body = document.querySelector("body");
const header = document.querySelector(".header");
const btnSub = document.querySelector(".header__menu-btn");
const menuLinks = document.querySelectorAll(".header__menu-link");


btnSub.addEventListener("click", () => {
    body.classList.toggle("overflow-hidden");  
    header.classList.toggle("nav-visible");    
});


menuLinks.forEach(link => {
    link.addEventListener("click", () => {
        body.classList.remove("overflow-hidden");  
        header.classList.remove("nav-visible");    
    });
});

