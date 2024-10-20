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