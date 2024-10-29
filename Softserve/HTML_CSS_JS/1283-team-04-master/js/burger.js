function initBurgerMenu() {
  const burgerButton = document.querySelector(".header__burger");
  const mobileMenu = document.querySelector(".header__mobile-menu");
  const closeButton = document.querySelector(".header__menu-close");

  if (burgerButton && mobileMenu && closeButton) {
    burgerButton.addEventListener("click", function () {
      mobileMenu.classList.add("header__mobile-menu--visible");
      document.body.classList.add('no-scroll');
    });

    closeButton.addEventListener("click", function () {
      mobileMenu.classList.remove("header__mobile-menu--visible");
      document.body.classList.remove('no-scroll');
    });
  }
}

initBurgerMenu();
