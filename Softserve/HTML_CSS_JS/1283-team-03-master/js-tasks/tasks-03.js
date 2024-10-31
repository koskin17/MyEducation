///////////////////https://www.codewars.com/kata/55a2d7ebe362935a210000b2

function findSmallestInt(arr) {
  return Math.min(...arr);
}


/////////////////////////https://www.codewars.com/kata/5722b3f0bd5583cf44001000

function giveMeFive(obj) {
  const arr = [];
  for(const key in obj) {
    if(key.length === 5) {
      arr.push(key);
    }
    if(obj[key].length === 5) {
      arr.push(obj[key]);
    }
  }
  return arr;
}


//////////https://www.codewars.com/kata/58e43389acfd3e81d5000a88/train/javascript

function circleCircumference(circle) {
  return +(2 * Math.PI * circle.radius).toFixed(6);
}


////////////////////////https://www.codewars.com/kata/56f935002e6c0d55fa000d92

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


////////////////////https://www.codewars.com/kata/56b71b1dbd06e6d88100092a

function buildFun(n) {
  const res = [];

  for(let i = 0; i < n; i++) {
    res.push(function () {
      return i;
    });
  }
  return res;
}