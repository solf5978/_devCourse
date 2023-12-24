'use strict';

const insertEveryN = function(arr, data, n) {
    let newArr = [...arr];
    let pos = 0;
    for (let _ = 0; _ < Math.floor(arr.length / n); _++) {
        pos = pos + n;
        newArr.splice(pos + _, 0, data);
    }
    return newArr;  
};

const insertEveryN_2 = function(arr, data, n) {
    return arr.flatMap((elem, idx) => (idx + 1) % n === 0 ? [elem, data] : elem);
};


const insertEveryN_3 = function(arr, data, n) {
    return arr.reduce((prevVal, currVal, idx) => 
    (Number.isInteger((idx + 1) / n)) ? [...prevVal, currVal, data] : [...prevVal, currVal], []);
};










// Testing insertEveryN...

console.assert(JSON.stringify(insertEveryN([50, 60, 90, 100, 20], 0, 2)) === JSON.stringify([50, 60, 0, 90, 100, 0, 20]), `insertEveryN first attempt!`);
console.assert(JSON.stringify(insertEveryN([true, true, true, true, true, true], false, 1)) === JSON.stringify([true, false, true, false, true, false, true, false, true, false, true, false]), `insertEveryN second attempt!`);
console.assert(JSON.stringify(insertEveryN(['james', 'mary', 'john', 'elise', 'jen', 'jess', 'anya'], 'steve', 3)) === JSON.stringify(['james', 'mary', 'john', 'steve', 'elise', 'jen', 'jess', 'steve', 'anya']), `insertEveryN third attempt!`);

console.assert(JSON.stringify(insertEveryN_2([50, 60, 90, 100, 20], 0, 2)) === JSON.stringify([50, 60, 0, 90, 100, 0, 20]), `insertEveryN first attempt!`);
console.assert(JSON.stringify(insertEveryN_2([true, true, true, true, true, true], false, 1)) === JSON.stringify([true, false, true, false, true, false, true, false, true, false, true, false]), `insertEveryN second attempt!`);
console.assert(JSON.stringify(insertEveryN_2(['james', 'mary', 'john', 'elise', 'jen', 'jess', 'anya'], 'steve', 3)) === JSON.stringify(['james', 'mary', 'john', 'steve', 'elise', 'jen', 'jess', 'steve', 'anya']), `insertEveryN third attempt!`);

console.assert(JSON.stringify(insertEveryN_3([50, 60, 90, 100, 20], 0, 2)) === JSON.stringify([50, 60, 0, 90, 100, 0, 20]), `insertEveryN first attempt!`);
console.assert(JSON.stringify(insertEveryN_3([true, true, true, true, true, true], false, 1)) === JSON.stringify([true, false, true, false, true, false, true, false, true, false, true, false]), `insertEveryN second attempt!`);
console.assert(JSON.stringify(insertEveryN_3(['james', 'mary', 'john', 'elise', 'jen', 'jess', 'anya'], 'steve', 3)) === JSON.stringify(['james', 'mary', 'john', 'steve', 'elise', 'jen', 'jess', 'steve', 'anya']), `insertEveryN third attempt!`);
