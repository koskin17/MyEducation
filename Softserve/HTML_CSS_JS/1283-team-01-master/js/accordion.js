document.querySelectorAll('.accordion__button').forEach(button => {
    button.addEventListener('click', () => {
        const accordionItem = button.parentElement;

        document.querySelectorAll('.accordion__item').forEach(item => {
            if (item !== accordionItem) {
                item.classList.remove('active');
                item.querySelector('.accordion__content').style.maxHeight = null;
            }
        });

        accordionItem.classList.toggle('active');
        const accordionContent = accordionItem.querySelector('.accordion__content');

        if (accordionItem.classList.contains('active')) {
            accordionContent.style.maxHeight = accordionContent.scrollHeight + "px";
        } else {
            accordionContent.style.maxHeight = null;
        }
    });
});