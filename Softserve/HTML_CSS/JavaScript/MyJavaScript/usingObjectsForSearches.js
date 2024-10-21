Використання об’єктів для пошуків
Об’єкти можна вважати сховищем ключів/значень, як словники. Якщо ви маєте табличні дані, для пошуку значень краще використати об’єкт, а не інструкцію switch чи ланцюжок if/else. В такому випадку найкраще, якщо ви знаєте, що ваші вхідні дані обмежені до певного діапазону.

Ось приклад об’єкта-публікації:

const article = {
  "title": "How to create objects in JavaScript",
  "link": "https://www.freecodecamp.org/news/a-complete-guide-to-creating-objects-in-javascript-b0e2450655e8/",
  "author": "Kaashan Hussain",
  "language": "JavaScript",
  "tags": "TECHNOLOGY",
  "createdAt": "NOVEMBER 28, 2018"
};

const articleAuthor = article["author"];
const articleLink = article["link"];

const value = "title";
const valueLookup = article[value];
articleAuthor є рядком Kaashan Hussain, articleLink є рядком https://www.freecodecamp.org/news/a-complete-guide-to-creating-objects-in-javascript-b0e2450655e8/, а valueLookup є рядком How to create objects in JavaScript.

Перетворіть інструкцію switch на об’єкт під назвою lookup. Використайте його, щоб знайти val та призначати пов’язаний рядок до змінної result.

// Налаштування
function phoneticLookup(val) {
  let result = "";

  // Змініть код лише під цим рядком
  const lookup = {
    "alpha": "Adams",
    "bravo": "Boston",
    "charlie": "Chicago",
    "delta": "Denver",
    "echo": "Easy",
    "foxtrot": "Frank"
  };

  result = lookup[val];
  return result;
}

phoneticLookup("charlie");