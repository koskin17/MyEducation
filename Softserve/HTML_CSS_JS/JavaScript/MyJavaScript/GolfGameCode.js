/* Гольф-код
У грі в гольф кожна лунка має par, що відповідає середній кількості ударів (strokes), які повинен зробити гравець, щоб забити м’яч у лунку та завершити гру. Існують різні псевдоніми залежно від того, де знаходяться ваші удари (strokes) відповідно до par.

Вашій функції буде передано аргументи par та strokes. Поверніть правильний рядок відповідно до цієї таблиці, в якій перелічено удари за пріоритетом зверху (найвищий) донизу (найнижчий):

    Удари	Повернений рядок
    1	    "Hole-in-one!"
<= par - 2	"Eagle"
par - 1	"Birdie"
par	"Par"
par + 1	"Bogey"
par + 2	"Double Bogey"
>= par + 3	"Go Home!"
par та strokes завжди будуть додатними числами. Ми додали масив усіх імен для вашої зручності.*/

function golfScore(par, strokes) {
    if (strokes === 1) {
      return "Hole-in-one!";
    } else if (strokes <= par - 2) {
      return "Eagle";
    } else if (strokes === par - 1) {
      return "Birdie";
    } else if (strokes === par) {
      return "Par";
    } else if (strokes === par + 1) {
      return "Bogey";
    } else if (strokes === par + 2) {
      return "Double Bogey";
    } else if (strokes >= par + 3) {
      return "Go Home!";
    }
  }