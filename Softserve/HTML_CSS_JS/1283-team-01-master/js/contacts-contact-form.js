const form = document.querySelector('.contact__form');
const userName = document.querySelector('.name');
const userPhone = document.querySelector('.phone');
const userEmail = document.querySelector('.email');
const userMessage = document.querySelector('.message');


// Show input error message
function showError(input, message) {
    console.log(`Помилка в полі: ${input.className}, повідомлення: ${message}`);
    const formControl = input;
    formControl.classList.add('error');
    const small = input.nextElementSibling;
    small.innerText = message;
}

// Show success outline
function showSuccess(input) {
  const formControl = input;
  formControl.classList.add('success');
}

// Check email is valid
function checkEmail(input) {
  const re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  if (re.test(input.value.trim())) {
    showSuccess(input);
  } else {
    showError(input, 'Email is not valid');
  }
}

// Check required fields
function checkRequired(inputArr) {
  inputArr.forEach(function(input) {
    if (input.value.trim() === '') {
      showError(input, `${getFieldName(input)} is required`);
    } else {
      showSuccess(input);
    }
  });
}

// Check input length
function checkLength(input, min, max) {
  if (input.value.length < min) {
    showError(
      input,
      `${getFieldName(input)} must be at least ${min} characters`
    );
  } else if (input.value.length > max) {
    showError(
      input,
      `${getFieldName(input)} must be less than ${max} characters`
    );
  } else {
    showSuccess(input);
  }
}

// Get fieldname
function getFieldName(input) {
  return input.placeholder.trim().split(" ").pop();
}


// Event listeners
form.addEventListener('submit', function(e) {
    e.preventDefault();

    // Видаляємо клас 'error' з усіх полів перед новою валідацією
    const errorElements = document.querySelectorAll('.error');
    errorElements.forEach(function(element) {
        element.classList.remove('error'); // Видаляємо клас 'error'
    });

    checkRequired([userName, userPhone, userEmail]);
    checkLength(userName, 3, 20);
    checkLength(userPhone, 6, 25);
    checkEmail(userEmail);
    
    // Якщо форма валідна, виводимо повідомлення
    if (formIsValid()) {
        alert("Thank you for reaching out! Please await our response."); // Показуємо повідомлення

        // Очищаємо клас 'success' з полів
        const successElements = document.querySelectorAll('.success');
        successElements.forEach(function(element) {
            element.classList.remove('success'); // Видаляємо клас 'success'
        });

        form.reset(); // Очищаємо форму після відправки
    }
});

function formIsValid() {
    const errorElements = document.querySelectorAll('.error');
    return errorElements.length === 0;
}