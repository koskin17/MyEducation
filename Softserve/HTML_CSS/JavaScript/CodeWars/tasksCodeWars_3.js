https://www.codewars.com/kata/find-the-smallest-integer-in-the-array/train/javascript
/* Find the smallest integer in the array
Given an array of integers your solution should find the smallest integer.

For example:

Given [34, 15, 88, 2] your solution will return 2
Given [34, -345, -1, 100] your solution will return -345
You can assume, for the purpose of this kata, that the supplied array will not be empty.

function findSmallestInt(arr) {
  return Math.min(...arr);
}
*/

https://www.codewars.com/kata/geometry-basics-circle-circumference-in-2d/train/javascript
/* Geometry Basics: Circle Circumference in 2D
This series of katas will introduce you to basics of doing geometry with computers.

Point objects have x, y attributes. Circle objects have center which is a Point, and radius, which is a number.

Write a function calculating circumference of a Circle.

Tests round answers to 6 decimal places.
Here's a JavaScript code that calculates the circumference of a circle based on the circle's center (which is a point) and radius. The circumference is calculated using the formula:

Circumference
=
2
×
𝜋
×
radius
Circumference=2×π×radius
We'll round the result to 6 decimal places as requested.

javascript
Копировать код
// Define a Point object
function Point(x, y) {
  this.x = x;
  this.y = y;
}

// Define a Circle object
function Circle(center, radius) {
  this.center = center;
  this.radius = radius;
}

// Function to calculate circumference of the circle
function calculateCircumference(circle) {
  // Formula for circumference: 2 * Math.PI * radius
  const circumference = 2 * Math.PI * circle.radius;
  // Rounding to 6 decimal places
  return parseFloat(circumference.toFixed(6));
}

// Example usage:
const center = new Point(0, 0);
const circle = new Circle(center, 5);
console.log(calculateCircumference(circle)); // Output: 31.415927
Explanation:
We first define a Point constructor to create a point with x and y coordinates.
The Circle constructor is defined to take a center (a Point object) and a radius.
The calculateCircumference function applies the formula for the circumference and rounds the result to 6 decimal places using toFixed(6).

one more variant const circleCircumference = circle => 2 * Math.PI * circle.radius;
*/

https://www.codewars.com/kata/training-js-number-12-loop-statement-for-dot-in-and-for-dot-of/train/javascript
/* Training JS #12: loop statement --for..in and for..of
In lesson #11, we learned that the for loop can be used to traverse an array.
If we want to traverse an object, we can use a variant of the for: for..in. This can traverse all the keys of the object. An example:

function showObjectKeys(obj){
  for (var key in obj){
    console.log(key);
  }
}
function showObjectValues(obj){
  for (var key in obj){
    console.log(obj[key]);
  }
}
var ob={item1:"This",item2:"is",item3:"an",item4:"example"};
console.log("keys of ob:")
showObjectKeys(ob);
console.log("values of ob:")
showObjectValues(ob);
Code results:

keys of ob:
item1
item2
item3
item4
values of ob:
This
is
an
example
for..in can also be used with arrays. Modifying the code above:

function showObjectKeys(obj){
  for (var key in obj){
    console.log(key);
  }
}
function showObjectValues(obj){
  for (var key in obj){
    console.log(obj[key]);
  }
}
var arr=["one","two","three"];
console.log("keys of arr:")
showObjectKeys(arr);
console.log("values of arr:")
showObjectValues(arr);
Code results:

keys of arr:
0
1
2
values of arr:
one
two
three
As you can see, the keys are the indices of the array elements.
Important: When using for..in with an array, the key (index) is always a string, not a number.
In the example above, the keys are "0", "1", and "2". We can't see the quotes because console.log() doesn't show them.

Although for..in can be used to traverse the array, this is discouraged because in some cases the order may be unexpected.
So it's recommended that you use another variant for this: for..of (new in ES6).
for..of can traverse all the values of the array (without accessing them through their index).
Function showObjectValues() from above can be modified like this:

function showArrayValues(arr){
  for (var value of arr){
    console.log(value);
  }
}
Ok, lesson is over, let's do a task with for..in.

Task
The function giveMeFive accepts 1 parameter, obj, which is an object.

Create an array (which you will eventually return).
Then, traverse obj, checking each key and value.
If the length of the key is equal to 5, then push the key to your array.
Separately, if the length of the value is equal to 5, then push the value to your array.

At the end, return your array.

You should use for..in in your code, otherwise your solution may not pass this kata.

Для решения задачи, где нужно использовать цикл for..in, мы можем следовать таким шагам:

Создаем пустой массив, который будет возвращать функция.
Используем цикл for..in, чтобы пройти по ключам объекта.
Если длина ключа равна 5, добавляем его в массив.
Если длина значения этого ключа равна 5, также добавляем его в массив.
Возвращаем массив в конце функции.
Вот пример решения:

javascript
Копировать код
function giveMeFive(obj) {
  // создаем пустой массив для хранения ключей и значений длиной 5
  const result = [];
  
  // используем for..in для перебора всех ключей объекта
  for (let key in obj) {
    // проверяем длину ключа
    if (key.length === 5) {
      result.push(key);
    }
    
    // проверяем длину значения
    if (obj[key].length === 5) {
      result.push(obj[key]);
    }
  }
  
  // возвращаем массив с результатами
  return result;
}
Пример использования:
javascript
Копировать код
const obj = {
  apple: "fruit",
  house: "home",
  table: "fives",
  car: "truck",
};

console.log(giveMeFive(obj)); 
// Ожидаемый результат: ["apple", "house", "fives"]
Объяснение:
Мы используем цикл for..in, чтобы пройти по всем ключам объекта.
Если длина ключа или значения равна 5, мы добавляем его в массив result.
В конце функция возвращает массив, содержащий все ключи и значения с длиной 5.

one more soltion:
function giveMeFive(obj){
  var five=[];
  for (var key in obj) {
    if (key.length==5) five.push(key);
    if (obj[key].length==5) five.push(obj[key]);
  }
  return five;
}
*/
