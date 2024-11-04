// https://www.codewars.com/kata/56f6ad906b88de513f000d96/train/javascript

function bonusTime(salary, bonus) {
  return "£" + (bonus ? salary * 10 : salary);
}

//https://www.codewars.com/kata/5264d2b162488dc400000001/javascript
function spinWords(string) {
  //TODO Have fun :)
  const str = string.split(" ");
  const new_str = [];

  str.forEach(function (el) {
    if (el.length >= 5) {
      new_str.push(el.split("").reverse().join(""));
    } else {
      new_str.push(el);
    }
  });

  return new_str.join(" ");
}

//spinWords("Hey fellow warriors");


// Messi Goals:
function goals(laLigaGoals, copaDelReyGoals, championsLeagueGoals) {
  return laLigaGoals + copaDelReyGoals + championsLeagueGoals;
}

// Make negative:
function makeNegative(num) {
   return num > 0 ? -num : num;
}

// Game Move:
function move(position, roll) {
  return position + roll * 2;
}

// Personalized Message:
function greet(name, owner) {
  return name === owner ? 'Hello boss' : 'Hello guest'
}

// Keep Hydrated:
function litres(time) {
  return Math.floor(time * 0.5);
}

 // Opposites Attract:
function lovefunc(flower1, flower2){
  return (flower1 % 2 !== flower2 % 2);
}
