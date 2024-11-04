const drawer_toggle = document.querySelectorAll('.menu__toggle');
const drawer = document.querySelector('.drawer');
const drawer_link = document.querySelectorAll('.drawer__menu a');


drawer_toggle.forEach(function (el) {
    el.addEventListener('click', function () {
        drawer.classList.toggle('drawer--show');
        this.classList.toggle('menu__toggle-active');
       
    });
});

drawer_link.forEach(function (el) {
    el.addEventListener('click', function () {
        drawer.classList.remove('drawer--show');
    });
});
