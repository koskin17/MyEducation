document.querySelectorAll(".faq-accordion__title").forEach((title) => {
  title.addEventListener("click", () => {
    const item = title.parentElement;

    // Закрити всі інші активні елементи
    document.querySelectorAll(".faq-accordion__item").forEach((i) => {
      if (i !== item) {
        i.classList.remove("faq-accordion__item--active");
      }
    });

    // Перемикати активний клас на обраному елементі
    item.classList.toggle("faq-accordion__item--active");
  });
});
