/* Search by tag is bad.
Correctly search for the class. */
const headerText = document.querySelector(".header__title");
/* Теперь есть переменная, в которую отбирается селектор header__title */

/* Создаем обычный список с вариантами приветствия */
const greetings = [
  "Hello, JS!",
  "Добрий день, JS!",
  "Bonjour, JS!",
  "Hola, JS!",
  "Ciao, JS!",
];

/* Создаём функцию, которая будет выбирать приветствие из списка */
function getRandomEl(arr) {
  /* Math.random генерирует случайное число от 0 до 1 и умножает его на длину списка, а потом округляет в меньшую сторону. В результате получаем индекс элемента из списка и пвозвращаем элемент из списка с этим индексом. */
  return arr[Math.floor(Math.random() * arr.length)];
}

/* Присваиваем новый текст приветствия переменной headerText и это текст будет отображён в момент загрузки страницы */
headerText.innerText = getRandomEl(greetings);
