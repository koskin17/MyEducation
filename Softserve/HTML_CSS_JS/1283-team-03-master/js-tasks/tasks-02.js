1; /////////////////https://www.codewars.com/kata/convert-a-string-to-an-array/train/javascript
function stringToArray(string) {
  return string.split(" ");
}

2; //////////////////https://www.codewars.com/kata/dna-to-rna-conversion/train/javascript
function DNAtoRNA(dna) {
  return dna
    .split("")
    .map((item) => (item === "T" ? "U" : item))
    .join("");
}

function DNAtoRNA(dna) {
  return dna.replaceAll("T", "U");
}

3; /////////////////https://www.codewars.com/kata/577a98a6ae28071780000989/train/javascript
const min = function (list) {
  return Math.min(...list);
};

const max = function (list) {
  return Math.max(...list);
};

4; ////////////////https://www.codewars.com/kata/544a54fd18b8e06d240005c0/train/javascript
function min(arr, toReturn) {
  return toReturn === "value"
    ? Math.min(...arr)
    : arr.indexOf(Math.min(...arr));
}

///////////////https://www.codewars.com/kata/53ee5429ba190077850011d4

function doubleInteger(i) {
  const result = i * 2;
  return result;
}

////////////////https://www.codewars.com/kata/5545f109004975ea66000086

function isDivisible(n, x, y) {
  return n % x === 0 && n % y === 0;
}

////////////////https://www.codewars.com/kata/5b853229cfde412a470000d0

function twiceAsOld(dadYearsOld, sonYearsOld) {
  return Math.abs(dadYearsOld - 2 * sonYearsOld);
}

//////////////https://www.codewars.com/kata/574b3b1599d8f897470018f6

function getRealFloor(n) {
  if (n > 0 && n <= 13) {
    return n - 1;
  } else if (n > 13) {
    return n - 2;
  } else {
    return n;
  }
}

///////////https://www.codewars.com/kata/5933a1f8552bc2750a0000ed

function nthEven(n) {
  return n * 2 - 2;
}

//////////////https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a

function past(h, m, s) {
  const secondsInHour = 3600;
  const secondsInMinute = 60;
  const millisecondsInSecond = 1000;
  return (h * secondsInHour + m * secondsInMinute + s) * millisecondsInSecond;
}
