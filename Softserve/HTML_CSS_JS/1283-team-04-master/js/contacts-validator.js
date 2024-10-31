const form = document.querySelector(".faq__form");
const username = document.querySelector(".faq__form-input.username");
const email = document.querySelector(".faq__form-input.e-mail");
const phone = document.querySelector(".faq__form-input.phone");
const textarea = document.querySelector(".faq__form-textarea");

form.addEventListener("submit", (e) => {
  e.preventDefault(); 
  const isValid = validateInputs(); 

  if (isValid) {
    const modal = new bootstrap.Modal(document.getElementById('staticBackdrop'));
    modal.show();
  }
});

const setError = (element, message) => {
  const inputControl = element.parentElement;
  const errorDisplay = inputControl.querySelector(".error");
  errorDisplay.innerText = message;
  inputControl.classList.add("error");
  inputControl.classList.remove("success");
};

const setSuccess = (element) => {
  const inputControl = element.parentElement;
  const errorDisplay = inputControl.querySelector(".error");
  errorDisplay.innerText = "";
  inputControl.classList.add("success");
  inputControl.classList.remove("error");
};

const isValidEmail = (email) => {
  const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return re.test(String(email).toLowerCase());
};

const isValidPhone = (phone) => {
  const phonePattern = /^(?:\+380|0)(\d{9})$/;
  return phonePattern.test(phone);
};

const validateUsername = (usernameValue) => {
  if (usernameValue === '') {
    setError(username, 'Username is required');
    return false;
  } else {
    setSuccess(username);
    return true;
  }
};

const validateEmail = (emailValue) => {
  if (emailValue === '') {
    setError(email, 'Email is required');
    return false;
  } else if (!isValidEmail(emailValue)) {
    setError(email, 'Email is not valid');
    return false;
  } else {
    setSuccess(email);
    return true;
  }
};

const validatePhone = (phoneValue) => {
  if (phoneValue === '') {
    setError(phone, 'Phone is required');
    return false;
  } else if (!isValidPhone(phoneValue)) {
    setError(phone, 'Phone is not valid');
    return false;
  } else {
    setSuccess(phone);
    return true;
  }
};

const clearInputs = () => {
  username.value = "";
  email.value = "";
  phone.value = "";
  textarea.value = "";
}

const validateInputs = () => {
  const usernameValue = username.value.trim();
  const emailValue = email.value.trim();
  const phoneValue = phone.value.trim();
  let isValid = true;

  isValid &= validateUsername(usernameValue);
  isValid &= validateEmail(emailValue);
  isValid &= validatePhone(phoneValue);

  if(isValid){
    clearInputs();
  }

  return isValid;
};
