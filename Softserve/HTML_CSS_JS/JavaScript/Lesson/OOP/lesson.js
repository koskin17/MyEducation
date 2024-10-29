const audiQ7 = {
  make: 'Audi',
  model: 'Q7',
  price: 60000,
  beep: function() {
    console.log(this.make + ' Beep!');
  },
  drive: function() {
    console.log(this.make + ' Drive!');
  }
};

// console.log(audiQ7);
// audiQ7.beep();
// console.log(audiQ7.make);
// audiQ7.drive();

// Класи
class Car {
  constructor(make, model, price) {
    this.make = make;
    this.model = model;
    this.price = price;
  }
  beep() {
    console.log(this.make + ' Beep!');
  }
  drive() {
    console.log(this.make + ' Drive!');
  }
}


const bmwX5 = new Car('BMW', 'X5', 50000);

// console.log(bmwX5);
// bmwX5.beep();
// bmwX5.drive();

const jeepRenegade = new Car('JEEP', 'Renegade', 15000);
console.log(JSON.stringify(jeepRenegade));

jeepRenegade.price = 16000;
console.log(jeepRenegade);


// JSON - JavaScript Object Notation
const jsonCar = `
{
  "make": "Audi",
  "model": "Q7",
  "price": 60000
}`;

const car = JSON.parse(jsonCar);
console.log(car);

// Поглиблена частина

// Нотація з квадратними дужками
const key = "model";
console.log(car[key]);

// Цикл
for (const key in car) {
  console.log(key, car[key]);
}

// Копіювання об'єктів
const car2 = car; // Не скопіюємо об'єкт, а лише його посилання
car2.model = 'A5';
console.log('car', JSON.stringify(car));
console.log('car2', JSON.stringify(car2));

const carCopy = {...car};
carCopy.model = 'A3';
console.log('car', JSON.stringify(car));
console.log('carCopy', JSON.stringify(carCopy));
// const carCopy = Object.assign({}, car);

// Глибоке копіювання
// const deepCopy = JSON.parse(JSON.stringify(car)); // Старий спосіб
// Новий спосіб - structuredClone
const deepCopy = structuredClone(car);
console.log(JSON.stringify(deepCopy));

// Приватні і статичні поля
// Наслідування
class ElectricCar extends Car {
  #battery;
  constructor(make, model, price, battery) {
    super(make, model, price);
    this.#battery = battery;
  }
  charge() {
    console.log(this.make + ' Charging...' + this.#battery);
  }
}

class HyperCar extends ElectricCar {
  #speed;
  constructor(make, model, price, battery, speed) {
    super(make, model, price, battery);
    this.#speed = speed;
  }
}

const teslaRoadster = new HyperCar('Tesla', 'Roadster', 1000000, 150, 400);
console.log(teslaRoadster);
teslaRoadster.charge();

const teslaX = new ElectricCar('Tesla', 'X', 90000, 100);
console.log(teslaX);
teslaX.drive();
teslaX.charge();


// Геттери і сеттери - для зміни значення властивості
class Person {
  constructor(firstName, lastName) {
    this.firstName = firstName;
    this.lastName = lastName;
  }
  get fullName() {
    return this.firstName + ' ' + this.lastName;
  }
  set fullName(newFullName) {
    [this.firstName, this.lastName] = newFullName.split(' ');
  }
}

const johnWeak = new Person('John', 'Weak');
johnWeak.fullName = 'Jon Snow';
console.log(johnWeak.firstName);
console.log(johnWeak.lastName);
console.log(johnWeak.fullName);

// Функція-конструктор
// function Car(make, model, price) {
//   this.make = make;
//   this.model = model;
//   this.price = price;
// }
// Car.prototype.beep = function() {
//   console.log(this.make + ' Beep!');
// }
// Car.prototype.drive = function() {
//   console.log(this.make + ' Drive!');
// }