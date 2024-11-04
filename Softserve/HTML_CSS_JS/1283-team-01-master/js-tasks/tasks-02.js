// https://www.codewars.com/kata/convert-a-string-to-an-array/train/javascript
function stringToArray(string){
    const stringArr = string.split(" ");
    return stringArr;
}

// https://www.codewars.com/kata/577a98a6ae28071780000989/train/javascript
var min = function(list){
    list.sort((a, b) => a - b);
    return list[0];
}

var max = function(list){
    list.sort((a, b) => b - a);
    return list[0];
}

// https://www.codewars.com/kata/544a54fd18b8e06d240005c0/train/javascript
function min(arr, toReturn) {
    let smallestValue = arr[0];
    let smallestIndex = 0;

    for (let i = 1; i < arr.length; i++) {
        if (arr[i] < smallestValue) {
            smallestValue = arr[i];
            smallestIndex = i;
        }
    }

    return toReturn === "value" ? smallestValue : smallestIndex;
}

// https://www.codewars.com/kata/dna-to-rna-conversion/train/javascript
function DNAtoRNA(dna) {
    let rna = '';

    for (let i = 0; i < dna.length; i++) {
        if (dna[i] === 'T') {
            rna += 'U';
        } else {
            rna += dna[i];
        }
    }

    return rna;
}

// You Can't Code Under Pressure #1
function doubleInteger(i) {
  return i*2;
}

// Twice as old
function twiceAsOld(dadYearsOld, sonYearsOld) {
  const twiceAgeOfSun=sonYearsOld*2;
  return Math.abs(dadYearsOld-twiceAgeOfSun);
}

// Return n-th even number
function nthEven(n){
  // your code here
  if(n>0){
  return (n-1)*2;
    }else{
      return "Wrong Value!";
    }
}


// What's the real floor
function getRealFloor(n) {
  if(n<=0){
    return n;
  }
  return n > 13 ? n - 2 : --n;
}

// Clock
function past(h, m, s){
  return (h*3600000)+(m*60000)+(s*1000);
}

//Is n divisible by x and y
function isDivisible(n, x, y) {
  return n%x===0 && n%y===0;
}
