const form = document.querySelector(".footer__contacts");
form.addEventListener("submit", handleSubmit);
  
async function handleSubmit(event) {
  event.preventDefault();
  const status = document.querySelector(".footer__contacts-status");
  const response = await fetch(event.target.action, {
    method: form.method,
    body: new FormData(event.target),
    headers: {
        'Accept': 'application/json'
    }
  })
  if (response.ok) {
      status.innerHTML = "Thanks for your submission!";
      form.reset()
    } else {
      status.innerHTML = "Oops! There was a problem submitting your form"
  }
}
