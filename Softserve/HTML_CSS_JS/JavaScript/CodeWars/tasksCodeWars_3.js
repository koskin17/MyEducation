/* https://www.codewars.com/kata/find-the-smallest-integer-in-the-array/train/javascript
Find the smallest integer in the array
Given an array of integers your solution should find the smallest integer.

For example:

Given [34, 15, 88, 2] your solution will return 2
Given [34, -345, -1, 100] your solution will return -345
You can assume, for the purpose of this kata, that the supplied array will not be empty.

function findSmallestInt(arr) {
  return Math.min(...arr);
}
*/

/* https://www.codewars.com/kata/geometry-basics-circle-circumference-in-2d/train/javascript
Geometry Basics: Circle Circumference in 2D
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

function calculateCircumference(circle) {
  const circumference = 2 * Math.PI * circle.radius;
  return parseFloat(circumference.toFixed(6));
}
  !!!
  Важно понимать и помнить, что функция toFixed в JS возвращает результат в виде строки и если нужно число, то придётся конвертировать её опять в число.
  Если в проекте нажен код, который будет работать быстро, то эти мелкие операции будут его тормозить.
  Текст можно отправлять только на web-страницу.
  Также тут можно не использовать const, а сразу делать return в виде формулы.

  Если в коде этой функции при передаче параметров взять circle в "{}", то это будет называться деструктуризация объекта.
  Т.е. ожидается, что на вход функции придёт объект, но мы можем просто указать назване ключа, который я хочу получить из этого объекта, что JS сделал переменную с этим именем.
  В итоге код сам создаёт переменную radius из объекта со значениями и предварительный расчёт результата, как и указание переменной не нужен.
  Метод деструктуризации объекта очень часто используется в React.
  function calculateCircumference({radius}) {
    return 2 * Marh.PI * radius;
}
    Последнее усовершенствование кода - сворачивание функции до стрелочки "=>"
  const circleCircumference = ({radius}) => 2 * Marh.PI * radius;
  
  !!!

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

/* https://www.codewars.com/kata/training-js-number-12-loop-statement-for-dot-in-and-for-dot-of/train/javascript
Training JS #12: loop statement --for..in and for..of
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
  !!!
    В JS всегда создаётся переменная не let, а const за исключением случаев, когда мы изначально знаем, что значение переменной будет меняться в коде.
    По этой причине и в цикле for переменная, которая каждый раз создаётся новая, нужно использовать const.
  !!!
  for (const key in obj) {
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

/* Задача про замыкание
https://www.codewars.com/kata/understanding-closures-the-basics/train/javascript
Understanding closures - the basics
This is a simple exercise to understand the feature in the javascript language called closure.
The function buildFun will return an array of functions. The single parameter accepted by buildFun is the number of elements N of the array returned.
The wanted outcome is that when all function in the array are executed, the number from 0 to N should be returned.

В этой задаче нужно написать функцию buildFun, которая принимает параметр N — количество элементов в возвращаемом массиве. Мы хотим, чтобы каждый элемент массива был функцией, которая при вызове возвращает свое значение от 0 до N.

Решение с использованием замыкания
!!! Замыкание - это защита от очистки памяти.
Замыкание поможет нам сохранить текущее значение индекса внутри каждой функции, когда она добавляется в массив.

function buildFun(N) {
  const result = [];
  
  for (let i = 0; i < N; i++) {
    result.push(function(i) {
      return i;
    });
  }
  return result;
}

const functions = buildFun(5);
console.log(functions[0]()); // Выведет 0
console.log(functions[1]()); // Выведет 1
console.log(functions[2]()); // Выведет 2
Почему это работает?
Использование let для переменной i в цикле for позволяет создать новое лексическое окружение для каждой итерации цикла. Это значит, что каждая функция, добавляемая в result, будет иметь свое собственное значение i, привязанное к конкретному замыканию.

Ещё одно решение:
const buildFun = n => [...Array(n)].map((v, i) => () => i);

Перед тем, как выполнять весь код, JS находит все var и всем им присваивает undefined.
После этого JS выполняет код строка за строкой.
Доходит до for, видит var и переназначает ей значение 0.
Потом переходит к добавлению в список функции, которая возвращает i. Если этой функции не передать i, то JS значение i из цикла for не увидит и вернуть ему будет нечего. В результате поиск начинается во внешней области видимости, которая как раз и является циклом for.
Предпоследняя итерация цикла for запишет в переменную i значение 9. Потом выполнит цикл.
Последняя итераци запишет в переменую i значение 10, но уже цикл не выполнится и в i останется значение 10.
Если же написать let, то JS не ищет никакие переменные var и не вытаскивает их, не готовит их в качестве коробочки для значений.
В результате переменная i создаётся только для цикла for и находися в области видимости только этого цикла и функции, которая в нём лежит.
*/

/* https://www.codewars.com/kata/fun-with-es6-classes-number-2-animals-and-inheritance/train/javascript
Задача про наследование.
Fun with ES6 Classes #2 - Animals and Inheritance
Overview
Preloaded for you in this Kata is a class Animal:

class Animal {
  constructor(name, age, legs, species, status) {
    this.name = name;
    this.age = age;
    this.legs = legs;
    this.species = species;
    this.status = status;
  }
  introduce() {
    return `Hello, my name is ${this.name} and I am ${this.age} years old.`;
  }
}
Task
Define the following classes that inherit from Animal.

I. Shark
The constructor function for Shark should accept 3 arguments in total in the following order: name, age, status. All sharks should have a leg count of 0 (since they obviously do not have any legs) and should have a species of "shark".

II. Cat
The constructor function for Cat should accept the same 3 arguments as with Shark: name, age, status. Cats should always have a leg count of 4 and a species of "cat".

Furthermore, the introduce/Introduce method for Cat should be identical to the original except there should be exactly 2 spaces and the words "Meow meow!" after the phrase. For example:

var example = new Cat("Example", 10, "Happy");
example.introduce() === "Hello, my name is Example and I am 10 years old.  Meow meow!"; // Notice the TWO spaces - very important
III. Dog
The Dog constructor should accept 4 arguments in the specified order: name, age, status, master. master is the name of the dog's master which will be a string. Furthermore, dogs should have 4 legs and a species of "dog".

Dogs have an identical introduce/Introduce method as any other animal, but they have their own method called greetMaster/GreetMaster which accepts no arguments and returns "Hello (insert_master_name_here)" (of course not the literal string but replace the (insert_master_name_here) with the name of the dog's master).

Вот решение для задачи с использованием классов и наследования в JavaScript:

class Animal {
  constructor(name, age, legs, species, status) {
    this.name = name;
    this.age = age;
    this.legs = legs;
    this.species = species;
    this.status = status;
  }
  introduce() {
    return `Hello, my name is ${this.name} and I am ${this.age} years old.`;
  }
}

class Shark extends Animal {
  constructor(name, age, status) {
    super(name, age, 0, "shark", status);
  }
}

class Cat extends Animal {
  constructor(name, age, status) {
    super(name, age, 4, "cat", status);
  }
  introduce() {
    return `${super.introduce()}  Meow meow!`;
  }
}

class Dog extends Animal {
  constructor(name, age, status, master) {
    super(name, age, 4, "dog", status);
    this.master = master;
  }
  greetMaster() {
    return `Hello ${this.master}`;
  }
}

// Примеры
const shark = new Shark("Sammy", 3, "Swimming freely");
console.log(shark.introduce()); // "Hello, my name is Sammy and I am 3 years old."

const cat = new Cat("Whiskers", 5, "Playful");
console.log(cat.introduce()); // "Hello, my name is Whiskers and I am 5 years old.  Meow meow!"

const dog = new Dog("Buddy", 4, "Loyal", "Alice");
console.log(dog.introduce()); // "Hello, my name is Buddy and I am 4 years old."
console.log(dog.greetMaster()); // "Hello Alice"
Объяснение:
Класс Shark: Конструктор принимает name, age, status и устанавливает legs в 0, а species в "shark".
Класс Cat: Конструктор также принимает name, age, status и устанавливает legs в 4, а species в "cat". Переопределенный метод introduce() добавляет "Meow meow!" после стандартного приветствия.
Класс Dog: Конструктор дополнительно принимает master, который сохраняется как свойство объекта. Метод greetMaster() возвращает приветствие с именем хозяина.

*/
