function initBurgerMenu() {
  const burgerButton = document.querySelector(".header__burger");
  const mobileMenu = document.querySelector(".header__mobile-menu");
  const closeButton = document.querySelector(".header__menu-close");
  const anchorLinks = document.querySelectorAll('a[href*="#"]');

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

  anchorLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      
      if (href.includes(window.location.pathname) || href.startsWith('#') || href.startsWith('./')) {
        const targetId = href.includes('#') ? href.split('#')[1] : '';
        const targetElement = document.getElementById(targetId);
        
        if (targetElement) {
          e.preventDefault();
          
          if (mobileMenu && mobileMenu.classList.contains('header__mobile-menu--visible')) {
            mobileMenu.classList.remove("header__mobile-menu--visible");
            document.body.classList.remove('no-scroll');
            
            setTimeout(() => {
              targetElement.scrollIntoView({ behavior: 'smooth' });
            }, 300);
          } else {
            targetElement.scrollIntoView({ behavior: 'smooth' });
          }
        }
      }
    });
  });

  /**
   * Scroll to the element with the given hash
   */
  function handleHashScroll() {
    if (window.location.hash) {
      const targetId = window.location.hash.slice(1);
      const targetElement = document.getElementById(targetId);
      
      if (targetElement) {
        setTimeout(() => {
          targetElement.scrollIntoView({ behavior: 'smooth' });
        }, 100);
      }
    }
  }

  handleHashScroll();
}

initBurgerMenu();
