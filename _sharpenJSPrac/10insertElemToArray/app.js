'use strict';

const insertEveryN = function(arr, data, n) {
  
};















// Testing insertEveryN...

console.assert(JSON.stringify(insertEveryN([50, 60, 90, 100, 20], 0, 2)) === JSON.stringify([50, 60, 0, 90, 100, 0, 20]), `insertEveryN first attempt!`);
console.assert(JSON.stringify(insertEveryN([true, true, true, true, true, true], false, 1)) === JSON.stringify([true, false, true, false, true, false, true, false, true, false, true, false]), `insertEveryN second attempt!`);
console.assert(JSON.stringify(insertEveryN(['james', 'mary', 'john', 'elise', 'jen', 'jess', 'anya'], 'steve', 3)) === JSON.stringify(['james', 'mary', 'john', 'steve', 'elise', 'jen', 'jess', 'steve', 'anya']), `insertEveryN third attempt!`);
