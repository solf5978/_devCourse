
const shuffleArray = function(arr) {
  let newArray = [...arr];

  return newArray;
};













// Testing shuffleArray...

console.assert(JSON.stringify(shuffleArray([1,2,3,4,5,6,7,8,9])) !== JSON.stringify([1,2,3,4,5,6,7,8,9]), `Array not shuffled!`);
let result = shuffleArray([1,2,3,4,5,6,7,8,9]);
console.assert((new Set(result)).size === result.length, `Array shuffled inaccurately!`);
