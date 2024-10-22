// Messi Goals  https://www.codewars.com/kata/grasshopper-messi-goals-function/train/javascript
function goals (laLigaGoals, copaDelReyGoals, championsLeagueGoals) {
    return laLigaGoals + copaDelReyGoals + championsLeagueGoals
  }

// Make negative https://www.codewars.com/kata/55685cd7ad70877c23000102/train/javascript
// My variant
function makeNegative(num) {
    if (num > 0) {
      return num *= -1;
    }
    return num;
  }

/* Variant 2
function makeNegative(num) {
    return num < 0 ? num : -num;
  }
*/

// Game Move https://www.codewars.com/kata/grasshopper-terminal-game-move-function/train/javascript

function move (position, roll) {
  return position + roll * 2
}

// Personalized Message https://www.codewars.com/kata/grasshopper-personalized-message/train/javascript

// My variant
function greet (name, owner) {
    if (name === owner) {
      return "Hello boss"
    } else {
      return "Hello guest"
    }
  }

/* Variant 2
function greet (name, owner) {
  return name === owner ? 'Hello boss' : 	'Hello guest';
}
  */

// Keep Hydrated https://www.codewars.com/kata/keep-hydrated-1/train/javascript
function litres(time) {
  return Math.floor(time * 0.5);
}

// Opposites Attract https://www.codewars.com/kata/555086d53eac039a2a000083/train/javascript
function areTheyInLove(flower1, flower2) {
  return (flower1 % 2 !== flower2 % 2);
}

/* New tasks */
/* https://www.codewars.com/kata/convert-a-string-to-an-array/train/javascript
Write a function to split a string and convert it into an array of words.

Examples (Input ==> Output):
"Robin Singh" ==> ["Robin", "Singh"]

"I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]
*/
function stringToArray(string) {
  return string.split(" ");
}

/* https://www.codewars.com/kata/dna-to-rna-conversion/train/javascript
DNA to RNA Conversion
Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').

Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from DNA its chemical structure and contains no Thymine. In RNA Thymine is replaced by another nucleic acid Uracil ('U').

Create a function which translates a given DNA string into RNA.

For example:

"GCAT"  =>  "GCAU"
The input string can be of arbitrary length - in particular, it may be empty. All input is guaranteed to be valid, i.e. each input string will only ever consist of 'G', 'C', 'A' and/or 'T'.
*/
function DNAtoRNA(dna) {
  return dna.includes("T") ? dna.prototype.replaceAll("T", "U") : dna;
}

/* https://www.codewars.com/kata/577a98a6ae28071780000989/train/javascript
Find Maximum and Minimum Values of a List
Your task is to make two functions ( max and min, or maximum and minimum, etc., depending on the language ) that receive a list of integers as input, and return the largest and lowest number in that list, respectively. Each function returns one number.

Examples (Input -> Output)
* [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
* [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
* [42, 54, 65, 87, 0]             -> min = 0, max = 87
* [5]                             -> min = 5, max = 5

При сортировке методы применяют к элементам списка метод String().
Из-за этого элементы, даже числа, сортируются как бы по алфавиту.
Избежать этого можно при помощи дополнительной функции, как sortEggsInNest(), к примеру.

Также сортировку можно реализовать:

const min = (list) => Math.min(...list);
const max = (list) => Math.max(...list);

Символы => — это стрелочная функция (arrow function) в JavaScript. Стрелочная функция — это более компактный синтаксис для записи функций. Вот эквивалентное объявление этих функций в традиционной форме:

const min = function(list) {
  return Math.min(...list);
};

const max = function(list) {
  return Math.max(...list);
};
Три точки перед list (...list)
Три точки перед именем переменной (...) — это оператор распаковки (spread operator). Он используется для распаковки элементов массива в отдельные значения.

В данном случае, ...list означает, что массив list передаётся в функцию Math.min() или Math.max() как набор отдельных значений, а не как один массив. Например:

javascript
Копировать код
const list = [1, 2, 3, 4];
Math.min(...list); // это то же самое, что Math.min(1, 2, 3, 4);
Таким образом:

Math.min(...list) находит минимальное значение в массиве.
Math.max(...list) находит максимальное значение в массиве.
*/
var min = function(list){
    function sortForMin(a, b) {
      return a > b ? 1 : b > a ? -1 : 0;
    }
    list = list.sort(sortForMin);
    return list[0];
}

var max = function(list){
    function sortForMax(a, b) {
      return a > b ? -1 : b > a ? 1 : 0;
    }
    list = list.sort(sortForMax);
    return list[0];
}

/*https://www.codewars.com/kata/544a54fd18b8e06d240005c0/train/javascript
Smallest value of an array
Write a function that can return the smallest value of an array or the index of that value. The function's 2nd parameter will tell whether it should return the value or the index.

Assume the first parameter will always be an array filled with at least 1 number and no duplicates. Assume the second parameter will be a string holding one of two values: 'value' and 'index'.

Some examples:

([1,2,3,4,5], "value") should return 1
([1,2,3,4,5], "index") should return 0
*/
function min(arr, toReturn) {
  if (toReturn === "value") {
    return Math.min(...arr);
  } else {
    return arr.indexOf(Math.min(...arr));
  }
}

/* https://www.codewars.com/kata/5b853229cfde412a470000d0/solutions/javascript
Twice as old
Your function takes two arguments:
- current father's age (years)
- current age of his son (years)

Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old). The answer is always greater or equal to 0, no matter if it was in the past or it is in the future.
*/
function twiceAsOld(dadYearsOld, sonYearsOld) {
  return Math.abs(dadYearsOld - (sonYearsOld * 2))
}

/* https://www.codewars.com/kata/5933a1f8552bc2750a0000ed/train/javascript
Get Nth Even Number
Return the Nth Even Number

Example(Input --> Output)

1 --> 0 (the first even number is 0)
3 --> 4 (the 3rd even number is 4 (0, 2, 4))
100 --> 198
1298734 --> 2597466
The input will not be 0.
*/
function nthEven(n){
  return (n * 2) - 2
}

/*https://www.codewars.com/kata/574b3b1599d8f897470018f6/train/javascript
What's the real floor?
Americans are odd people: in their buildings, the first floor is actually the ground floor and there is no 13th floor (due to superstition).

Write a function that given a floor in the american system returns the floor in the european system.

With the 1st floor being replaced by the ground floor and the 13th floor being removed, the numbers move down to take their place. In case of above 13, they move down by two because there are two omitted numbers below them.

Basements (negatives) stay the same as the universal level.

function getRealFloor(n) {
  return n > 13 ? n - 2 : n > 0 ? n - 1 : n;
}
*/
function getEuropeanFloor(americanFloor) {
  if (americanFloor <= 0) {
    // Basements (negative floors) stay the same
    return americanFloor;
  } else if (americanFloor < 13) {
    // For floors from 1 to 12, subtract 1 (since the 1st floor is the ground floor)
    return americanFloor - 1;
  } else {
    // For floors above 13, subtract 2 (since both the 1st floor and the 13th floor are skipped)
    return americanFloor - 2;
  }
}

/* https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a/train/javascript
Beginner Series #2 Clock
Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.
h = 0
m = 1
s = 1

result = 61000
function past(h, m, s){
  return ((h*3600)+(m*60)+s)*1000;
}
*/
function past(h, m, s) {
  // Convert hours to milliseconds: 1 hour = 3600000 milliseconds
  const hoursToMilliseconds = h * 3600000;
  // Convert minutes to milliseconds: 1 minute = 60000 milliseconds
  const minutesToMilliseconds = m * 60000;
  // Convert seconds to milliseconds: 1 second = 1000 milliseconds
  const secondsToMilliseconds = s * 1000;

  // Return the total time in milliseconds since midnight
  return hoursToMilliseconds + minutesToMilliseconds + secondsToMilliseconds;
}

/* console.log(past(0, 1, 1));   // Output: 61000 (1 minute and 1 second = 61000 milliseconds)
console.log(past(1, 0, 0));   // Output: 3600000 (1 hour = 3600000 milliseconds)
console.log(past(0, 0, 0));   // Output: 0 (midnight)
console.log(past(23, 59, 59)); // Output: 86399000 (one second before midnight)
Explanation:
1 hour = 3600000 milliseconds (60 minutes * 60 seconds * 1000 milliseconds).
1 minute = 60000 milliseconds (60 seconds * 1000 milliseconds).
1 second = 1000 milliseconds.
By multiplying the given hours, minutes, and seconds by their respective conversions and summing them, the function returns the total time in milliseconds since midnight.
*/

/* https://www.codewars.com/kata/5545f109004975ea66000086/train/javascript
Create a function that checks if a number n is divisible by two numbers x AND y. All inputs are positive, non-zero numbers.

Examples:
1) n =   3, x = 1, y = 3 =>  true because   3 is divisible by 1 and 3
2) n =  12, x = 2, y = 6 =>  true because  12 is divisible by 2 and 6
3) n = 100, x = 5, y = 3 => false because 100 is not divisible by 3
4) n =  12, x = 7, y = 5 => false because  12 is neither divisible by 7 nor 5
*/
function isDivisible(n, x, y) {
  if (n % x === 0 && n % y === 0) {
    return true;
  } else {
    return false;
  }
// еще один вариант: return (n % x === 0 && n % y === 0) ? true : false;
}


/* Freecodecamp tasks */
/*
Step 1
A teacher has finished grading their students' tests and needs your help to calculate the average score for the class.

Complete the getAverage function which takes in an array of test scores and returns the average score.

The average is calculated by adding up all the scores and dividing by the total number of scores.

Example Code
average = sum of all scores / total number of scores
A couple of function calls have been provided for you so you can test out your code.

Tips

You can use a loop to iterate over the scores array and add up all the scores.
You can use the length property to get the total number of scores.
*/
function getAverage(scores) {
  let sumOfScores = 0;
  for (let i = 0; i < scores.length; i++) {
    sumOfScores += scores[i];
  }
  return sumOfScores / scores.length;
}

console.log(getAverage([92, 88, 12, 77, 57, 100, 67, 38, 97, 89]));
console.log(getAverage([45, 87, 98, 100, 86, 94, 67, 88, 94, 95]));

/*
Step 2
Now the teacher needs your help converting the student score to a letter grade.

Complete the getGrade function that takes a number score as a parameter. Your function should return a string representing a letter grade based on the score.

Here are the scores and their corresponding letter grades:

Score Range	Grade
100	"A++"
90 - 99	"A"
80 - 89	"B"
70 - 79	"C"
60 - 69	"D"
0 - 59	"F"
Tips

Remember that you learned about conditional statements (if, else if, and else).
Remember that you learned about comparison operators (>, <, >=, <=, ===).

Метод switch не поддерживает сравнение и пределы сравнений 0 < var < 10.
В случае, если нужно проверять на нахождение в пределе, то надо использоваться конструкции if...else
*/
function getGrade(score) {
  if (score === 100) {
    return "A++";
  } else if (score >= 90 && score <= 99) {
    return "A";
  } else if (score >= 80 && score <= 89) {
    return "B";
  } else if (score >= 70 && score <= 79) {
    return "C";
  } else if (score >= 60 && score <= 69) {
    return "D";
  } else if (score >= 0 && score <= 59) {
    return "F";
  } else {
    return "Invalid score";
  }
}

/* Step 3
The teacher is really happy with the program you have created so far. But now they want to have an easy way to check if a student has a passing grade. A passing grade is anything that is not an "F".

Complete the function hasPassingGrade that takes a student score as a parameter. Your function should return true if the student has a passing grade and false if they do not.

Tips

Use the getGrade function to get the student's grade. Then check if the grade is passing or not.
*/
function hasPassingGrade(score) {
  let grade = getGrade(score);
  if (grade !== "F") {
    return true;
  } else {
    return false;
  }
}


console.log(hasPassingGrade(100));
console.log(hasPassingGrade(53));
console.log(hasPassingGrade(87));

/*Step 4
Now that the teacher has all of the information they need, they want to be able to message the student with the results.

Complete the studentMsg function with totalScores and studentScore for parameters. The function should return a string representing a message to the student.

If the student passed the course, the string should follow this format:

Example Code
Class average: average-goes-here. Your grade: grade-goes-here. You passed the course.
If the student failed the course, the string should follow this format:

Example Code
Class average: average-goes-here. Your grade: grade-goes-here. You failed the course.
Replace average-goes-here with the average of the total scores. Replace grade-goes-here with the student's grade.

Tips

Use the getAverage function to get the class average.
Use the getGrade function to get the student's grade.
Use string concatenation (+) to build the message.
Be careful with the punctuation and spaces in the message.
*/

function studentMsg(totalScores, studentScore) {
  let grade = hasPassingGrade(studentScore);
  if (grade) {
    return "Class average: " + getAverage(totalScores) + ". Your grade: " + getGrade(studentScore) + ". You passed the course."
  } else {
    return "Class average: " + getAverage(totalScores) + ". Your grade: " + getGrade(studentScore) + ". You failed the course."
  }
}

console.log(studentMsg([92, 88, 12, 77, 57, 100, 67, 38, 97, 89], 37));