/*
Перевірка властивостей об’єктів
Щоб перевірити, чи існує властивість даного об’єкта, ви можете скористатися методом .hasOwnProperty(). someObject.hasOwnProperty(someProperty) повертає true або false залежно від того, знайдено властивість в об’єкті чи ні.

Приклад

function checkForProperty(object, property) {
  return object.hasOwnProperty(property);
}

checkForProperty({ top: 'hat', bottom: 'pants' }, 'top'); // true
checkForProperty({ top: 'hat', bottom: 'pants' }, 'middle'); // false
Перший виклик функції checkForProperty повертає true, а другий повертає false.

Змініть функцію checkObj так, щоб вона перевіряла, чи переданий до функції параметр obj містить певну властивість, передану параметру функції checkProp. Якщо властивість, передану до checkProp, знайдено в obj, поверніть значення цієї властивості. Якщо ні, поверніть Not Found.

Запустити тест (Ctrl + Enter)
Скинути цей урок
Отримати допомогу
Тести
Пройдено:1. checkObj({gift: "pony", pet: "kitten", bed: "sleigh"}, "gift") має повертати рядок pony.
Пройдено:2. checkObj({gift: "pony", pet: "kitten", bed: "sleigh"}, "pet") має повертати рядок kitten.
Пройдено:3. checkObj({gift: "pony", pet: "kitten", bed: "sleigh"}, "house") має повертати рядок Not Found.
Пройдено:4. checkObj({city: "Seattle"}, "city") має повертати рядок Seattle.
Пройдено:5. checkObj({city: "Seattle"}, "district") має повертати рядок Not Found.
Пройдено:6. checkObj({pet: "kitten", bed: "sleigh"}, "gift") має повертати рядок Not Found.
*/

function checkObj(obj, checkProp) {
  if (obj.hasOwnProperty(checkProp)) {
    return obj[checkProp];
  } else {
    return "Not Found";
  }
}