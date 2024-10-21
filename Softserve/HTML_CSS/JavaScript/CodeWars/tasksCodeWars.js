// https://www.codewars.com/kata/53af2b8861023f1d88000832/train/javascript
function areYouPlayingBanjo(name) {
    if (name[0].toLowerCase() === "r") {
        return name + " plays banjo";
    } else {
        return name + " does not play banjo";
    }
  }

/*
function areYouPlayingBanjo(name) {
  return name + (name[0].toLowerCase() == r ?  plays :  does not play) + " banjo";
}
*/

// https://www.codewars.com/kata/596c6eb85b0f515834000049/train/javascript
function replaceDots(str) {
    newStr = str.replaceAll(".", "-");
    return newStr;
  }
/*
var replaceDots = function(str) {
// added the \ to escape special characters
// added the g so that replace is run for all occurences in the string
  return str.replace(/\./g, -);
}
*/

// https://www.codewars.com/kata/5808dcb8f0ed42ae34000031/train/javascript
function switchItUp(number){
    switch (number) {
        case 1:
            return "One";
        case 2:
            return "Two";
        case 3:
            return "Three";
        case 4:
            return "Four";
        case 5:
            return "Five";
        case 6:
            return "Six";
        case 7:
            return "Seven";
        case 8:
            return "Eight";
        case 9:
            return "Nine";
        case 0:
            return "Zero";
    }
}
// switchItUp=n=>["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"][n]
/*
function switchItUp(number) {
  switch (number) {
    case 0: return 'Zero';
    case 1: return 'One';
    case 2: return 'Two';
    case 3: return 'Three';
    case 4: return 'Four';
    case 5: return 'Five';
    case 6: return 'Six';
    case 7: return 'Seven';
    case 8: return 'Eight';
    case 9: return 'Nine';
  }
}
*/

// https://www.codewars.com/kata/57faece99610ced690000165
function remove(string) {  
    while (string.endsWith("!")) {
        string = string.slice(0, string.length - 1); // Убираем последний символ
    }
    return string; // Возвращаем строку после завершения цикла
}

// Используем регулярное выражение для удаления всех восклицательных знаков в конце строки
// return sentence.replace(/!+$/, '');