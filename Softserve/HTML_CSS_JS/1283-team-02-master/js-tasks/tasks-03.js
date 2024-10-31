// https://www.codewars.com/kata/find-the-smallest-integer-in-the-array/train/javascript
// Andrii Ferenchuk
function findSmallestInt(arr) {
    const copyArr = [...arr]
    return copyArr.sort((a, b) => a - b)[0]
}
// https://www.codewars.com/kata/geometry-basics-circle-circumference-in-2d/train/javascript
// Andrii Ferenchuk
function circleCircumference(circle) {
    const circumference = circle.radius * Math.PI * 2;
    return circumference.toFixed(6);
}
https://www.codewars.com/kata/training-js-number-12-loop-statement-for-dot-in-and-for-dot-of/train/javascript
// Andrii Ferenchuk
function giveMeFive(obj) {
    const array = []
    for (const key in obj) {
        console.log(key);
        if (key.length === 5) {
            array.push(key)
        }
        if (obj[key].length === 5) {
            array.push(obj[key])
        }
    }
    return array
}
// https://www.codewars.com/kata/understanding-closures-the-basics/train/javascript
// Andrii Ferenchuk
function buildFun(n) {
    let res = []
    for (let i = 0; i < n; i++) {
        res.push(function () {
            console.log(i);
        });
    }
    return res
}
https://www.codewars.com/kata/fun-with-es6-classes-number-2-animals-and-inheritance/train/javascript
// Andrii Ferenchuk
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
        return `${super.introduce()} Meow meow!`;
    }
}

class Dog extends Animal {
    constructor(name, age, status, master) {
        super(name, age, 4, "dog", status);
        this.master = master;
    }
    greetMaster() {
        return `Hello ${this.master}`
    }
}
