// Messi Goals https://www.codewars.com/kata/grasshopper-messi-goals-function/train/javascript
// solution | Andrii Ferenchuk
function goals(laLigaGoals, copaDelReyGoals, championsLeagueGoals) {
    return laLigaGoals + copaDelReyGoals + championsLeagueGoals;
}
// solution | Kostya Zeykin
function goals(laLigaGoals, copaDelReyGoals, championsLeagueGoals) {
    return laLigaGoals + copaDelReyGoals + championsLeagueGoals
}
// solution | Yehor Honcharenko
const goals = (laLigaGoals, copaDelReyGoals, championsLeagueGoals) =>
    laLigaGoals + copaDelReyGoals + championsLeagueGoals;
// solution | Diakov Roman
function goals(laLigaGoals, copaDelReyGoals, championsLeagueGoals) {
  return Number(laLigaGoals) + Number(copaDelReyGoals) + Number(championsLeagueGoals);
}
// solution | Krystyna Lebid
function goals (laLigaGoals, copaDelReyGoals, championsLeagueGoals) {
  return (laLigaGoals + copaDelReyGoals + championsLeagueGoals);
}
//solution | Mykyta Mantsov
function goals(laLigaGoals, copaDelReyGoals, championsLeagueGoals) {
  return laLigaGoals + copaDelReyGoals + championsLeagueGoals;
}

// Make negative https://www.codewars.com/kata/55685cd7ad70877c23000102/train/javascript
// solution | Andrii Ferenchuk
function makeNegative(num) {
    return num >= 0 ? num * (-1) : num;
}
// solution | Kostya Zeykin
function makeNegative(num) {
  return -Math.abs(num);
}
// solution | Yehor Honcharenko
function makeNegative(num) {
    return num > 0 ? num - (num * 2) : num;
  }
// solution | Diakov Roman
function makeNegative(num) {
  if (num <= 0) {
    return num;
  } else {
    return -num;
  }
}
// solution | Krystyna Lebid
function makeNegative(num) {
  if (num <= 0) {
    return num;
  } else {
    return -num;
  }
}
// solution | Mykyta Mantsov
function makeNegative(num) {
  return num <= 0 ? num: -num
}

// Game Move  https://www.codewars.com/kata/grasshopper-terminal-game-move-function/train/javascript
// solution | Andrii Ferenchuk
function move(position, roll) {
    return position + roll * 2;
}
// solution | Kostya Zeykin
function move(position, roll) {
    return position + roll * 2
  }
// solution | Yehor Honcharenko
const move = (position, roll) =>
    position + roll*2;
// solution | Diakov Roman
function move(position, roll) {
  return position + roll * 2;
}
// solution | Krystyna Lebid
function move (position, roll) {
  return position + (roll * 2);
}
// solution | Mykyta Mantsov
function move (position, roll) {
  return position + roll * 2
}

// Personalized Message https://www.codewars.com/kata/grasshopper-personalized-message/train/javascript
// solution | Andrii Ferenchuk
function greet(name, owner) {
    return name === owner ? 'Hello boss' : 'Hello guest';
}
// solution | Kostya Zeykin
function greet(name, owner) {
  return "Hello " + (name === owner ? "boss" : "guest");
  // лучший вариант - return "Hello ${name === owner ? "boss" : "guest"}";
}
// solution | Yehor Honcharenko
const greet = (name,owner) =>
    name === owner ? "Hello boss" : "Hello guest";
// solution | Diakov Roman
function greet(name, owner) {
  if (name === owner) {
    return "Hello boss";
  } else {
    return "Hello guest";
  }
}
// solution | Krystyna Lebid
function greet (name, owner) {
  if (name === owner) {
    return "Hello boss";
  } else {
    return "Hello guest";
  }
}
// solution | Mykyta Mantsov
function greet (name, owner) {
  return name === owner ? 'Hello boss' : 'Hello guest';
}

// Keep Hydrated https://www.codewars.com/kata/keep-hydrated-1/train/javascript
// solution | Andrii Ferenchuk

function litres(time) {
    return Math.floor(time * (0.5));
}
// solution | Kostya Zeykin
function litres(time) {
    return Math.floor(time * 0.5);
}
// solution | Yehor Honcharenko
const litres = (time) =>
    Math.floor(time * 0.5);
// solution | Diakov Roman
function litres(time) {
  return Math.floor(time * 0.5);
}
// solution | Krystyna Lebid
function litres(time) {
  return Math.floor(time * 0.5);
}
// solution | Mykyta Mantsov
function litres(time) {
  return Math.floor(time * 0.5);
}

// Opposites Attract https://www.codewars.com/kata/555086d53eac039a2a000083/train/javascript
// solution | Andrii Ferenchuk
function lovefunc(flower1, flower2) {
    return ((flower1 + flower2) % 2 !== 0);
}
// solution | Kostya Zeykin
function areTheyInLove(flower1, flower2) {
    return (flower1 % 2 !== flower2 % 2);
}
// solution | Yehor Honcharenko
const lovefunc = (flower1, flower2) =>
    flower1 % 2 !== flower2 % 2;
// solution | Diakov Roman
function lovefunc(flower1, flower2) {
  return flower1 % 2 !== flower2 % 2;
}
// solution | Krystyna Lebid
function lovefunc(flower1, flower2){
  return ((flower1 + flower2) % 2 !== 0);
}
// solution | Mykyta Mantsov
function lovefunc(flower1, flower2){
  return (flower1 % 2 !== flower2 % 2);
}