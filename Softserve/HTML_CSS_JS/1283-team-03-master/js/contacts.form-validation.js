document
  .querySelector(".contacts-form__form")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    let valid = true;
    const errorMessage = document.querySelector(
      ".contacts-form__error-message"
    );
    errorMessage.style.display = "none";

    const name = document.querySelector(".your-name").value.trim();
    if (name === "") {
      valid = false;
    }

    const phone = document.querySelector(".phone-number").value.trim();
    const phoneRegex = /^\+?[0-9\s-]{7,15}$/;
    if (!phoneRegex.test(phone)) {
      valid = false;
    }

    const email = document.querySelector(".email").value.trim();
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      valid = false;
    }

    if (valid) {
      alert("Form submitted successfully!");
    } else {
      errorMessage.style.display = "block";
    }
  });
