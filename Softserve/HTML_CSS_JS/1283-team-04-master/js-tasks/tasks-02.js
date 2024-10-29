/**
 * #1. Convert a string to an array
 * https://www.codewars.com/kata/convert-a-string-to-an-array/train/javascript
 *
 * @param {string} string
 * @returns {string[]}
 */
function stringToArray(string) {
  return string.split(" ");
}

/**
 * #2. DNA to RNA Conversion
 * https://www.codewars.com/kata/dna-to-rna-conversion/train/javascript
 *
 * @param {string} dna
 * @returns {string}
 */
function DNAtoRNA(dna) {
  return dna.replaceAll("T", "U");
}

/**
 * #3. Find Maximum and Minimum Values of a List
 * https://www.codewars.com/kata/577a98a6ae28071780000989/train/javascript
 */

const min = function (list) {
  list.sort((a, b) => a - b);

  return list[0];
};

const max = function (list) {
  list.sort((a, b) => b - a);

  return list[0];
};

/**
 * #4. Smallest value of an array
 * https://www.codewars.com/kata/544a54fd18b8e06d240005c0/train/javascript
 *
 * @param {number[]} arr
 * @param {string} toReturn
 * @returns {number}
 */
function min(arr, toReturn) {
  let minValue = Math.min(...arr);

  return toReturn === "index"
    ? arr.findIndex((value) => value === minValue)
    : minValue;
}
