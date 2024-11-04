// https://www.codewars.com/kata/find-the-smallest-integer-in-the-array/train/javascript
class GetMinNumb {
  findSmallestInt = args => Math.min(...args);
}

// https://www.codewars.com/kata/geometry-basics-circle-circumference-in-2d/train/javascript
function circleCircumference(circle) {
  const radius = circle.radius;
  const circumference = 2 * Math.PI * radius;
  return Number(circumference.toFixed(6));
}

// https://www.codewars.com/kata/training-js-number-12-loop-statement-for-dot-in-and-for-dot-of/train/javascript
function giveMeFive(obj) {
  const arr = [];
  for (let key in obj) {
      if (key.length === 5) {
          arr.push(key);
      }
      if (obj[key].length === 5) {
          arr.push(obj[key]);
      }
  }
  return arr;
}

// https://www.codewars.com/kata/understanding-closures-the-basics/train/javascript
function buildFun(n) {
  var res = [];

  for (var i = 0; i < n; i++) {
    res.push((function(i) {
      return function() {
        return i; 
      };
    })(i)); 
  }

  return res;
}

// https://www.codewars.com/kata/fun-with-es6-classes-number-2-animals-and-inheritance/train/javascript
class Animal {
  constructor(name, age, legs, species, status) {
    this.name = name;
    this.age = age;
    this.legs = legs;
    this.species = species;
    this.status = status;
  }
  introduce() {
    return Hello, my name is ${this.name} and I am ${this.age} years old.;
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
    return ${super.introduce()}  Meow meow!; 
  }
}

class Dog extends Animal {
  constructor(name, age, status, master,) {
    super(name, age, 4, "dog", status);
    this.master = master;
  }
  greetMaster() {
    return Hello ${this.master};
  }
}
