'use strict';

const totalLength = function(array) {
    let tempLen = 0;
    for (let elem of array) {
        if (Array.isArray(elem)) {
            tempLen = tempLen +totalLength(elem);
        } else {
            tempLen++;
        }
    }
    return tempLen;
};


















// Testing totalLength...

console.assert(totalLength([1,2,[3,4,5,[6,7,[12]]],8,9,[10,11]]) === 12, `totalLength first attempt!`);
console.assert(totalLength([true, true, true, true, true, true]) === 6, `totalLength second attempt!`);
console.assert(totalLength(['james', 'mary', 'john',['ann','jose',['ralph',[['agatha']]]], 'elise', 'jen', 'jess', 'anya']) === 11, `totalLength third attempt!`);
console.assert(totalLength([[[[[1]]]]]) === 1, `totalLength fourth attempt!`);