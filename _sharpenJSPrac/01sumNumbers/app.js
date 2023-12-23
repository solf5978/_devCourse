// // Solution 1 Using Object Arguments
const sumEverything = function() {
  // Object arg*
  let total = 0;
  for (let number of arguments) {
    total = total + number;
  }
  return total;
};

// Solution 2 Using Reduce
const sumEverything_1 = function() {
    return Array.from(arguments).reduce((prevNum, currNum) => prevNum + currNum, 0);
};

// Solution 3 Using Rest
const sumEverything_2 = function(...nums) {
    return nums.reduce ((prevNum, currNum) => prevNum + currNum, 0);
}










// Testing sumEverything...

console.assert(sumEverything(5, 5, 5, 5, 0) === 20, `summing everything first attempt!`);
console.assert(sumEverything(1, 2, 3, 4, 5, 6, 7) === 28, `summing everything second attempt!`);
console.assert(sumEverything(-1, -5, 10, 500, 60) === 564, `summing everything third attempt!`);
console.assert(sumEverything_1(5, 5, 5, 5, 0) === 20, `summing everything first attempt!`);
console.assert(sumEverything_1(1, 2, 3, 4, 5, 6, 7) === 28, `summing everything second attempt!`);
console.assert(sumEverything_1(-1, -5, 10, 500, 60) === 564, `summing everything third attempt!`);
console.assert(sumEverything_2(5, 5, 5, 5, 0) === 20, `summing everything first attempt!`);
console.assert(sumEverything_2(1, 2, 3, 4, 5, 6, 7) === 28, `summing everything second attempt!`);
console.assert(sumEverything_2(-1, -5, 10, 500, 60) === 564, `summing everything third attempt!`);
