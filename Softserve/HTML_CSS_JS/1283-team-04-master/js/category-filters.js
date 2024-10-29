document.getElementById('filtersToggle').addEventListener('click', function() {
    document.getElementById('filtersSidebar').classList.add('filters--open');
    document.body.classList.add('no-scroll');
});

document.getElementById('filtersClose').addEventListener('click', function() {
    document.getElementById('filtersSidebar').classList.remove('filters--open');
    document.body.classList.remove('no-scroll');
});

const accordionButtons = document.querySelectorAll('.accordion__button');
accordionButtons.forEach(button => {
    button.addEventListener('click', () => {
        const content = button.nextElementSibling;
        button.classList.toggle('accordion__button--active');
        if (content.style.maxHeight) {
            content.style.maxHeight = null;
        } else {
            content.style.maxHeight = content.scrollHeight + 'px';
        }
    });
});