const headerText = document.querySelector(".header__title");

const greetings = [
  "Hello, JS!",
  "Добрий день, JS!",
  "Bonjour, JS!",
  "Hola, JS!",
  "Ciao, JS!",
];

function getRandomEl(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}

headerText.innerText = getRandomEl(greetings);
