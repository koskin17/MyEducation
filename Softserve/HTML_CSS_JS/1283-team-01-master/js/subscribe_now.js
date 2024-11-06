// Отримуємо форму та елементи
const form = document.querySelector('.subscribe-now__form');
const emailInput = form.querySelector('.subscribe-now__input');
const submitButton = form.querySelector('.subscribe-now__button');

// Функція перевірки формату e-mail
function validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Додаємо перевірку при відправленні форми
form.addEventListener('submit', (event) => {
    const emailValue = emailInput.value.trim();
    
    if (!validateEmail(emailValue)) {
        event.preventDefault();  // Блокуємо відправку форми
        emailInput.focus();      // Переміщуємо фокус на поле email
        alert('Будь ласка, введіть правильний формат email');
    } else {
        // Імітація успішної відправки форми
        console.log("Форма відправлена! Email:", emailValue);
        
        // Можемо також показати користувачу alert про успішну відправку
        alert('Дякуємо за підписку!');
    }
});