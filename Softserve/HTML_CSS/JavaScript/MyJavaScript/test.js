function nextInLine(arr, item) {
    // Змініть код лише під цим рядком
    arr.push(6);
    return arr.shift();
    // Змініть код лише над цим рядком
  }
  
  // Налаштування
  let testArr = [1, 2, 3, 4, 5];
  
  // Відобразити код
  console.log("Before: " + JSON.stringify(testArr));
  console.log(nextInLine(testArr, 6));
  console.log("After: " + JSON.stringify(testArr));