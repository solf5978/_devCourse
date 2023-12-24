'use strict';

const removeFalseys = function(arry) {
    let newArr = [];
    for (let val of arry) {
        if (!val) {
            continue;
        } else {
            newArr.push(val)
        }
    }
    return newArr;
};

//  From Instructor
const removeFalseys_1 = function(arry) {
    let newArr = [];
    for (let elem of arry) {
        if (elem) newArr.push(elem);
    }
    return newArr;
}

//  Solution 2
const removeFalseys_2 = function(arry) {
    let newArr = [];
    arry.forEach(elem => elem && newArr.push(elem));
    return newArr;
}

const removeFalseys_3 = function(arry) {
    return arry.filter(elem => elem);
}












// Testing removeFalseys...

console.assert(JSON.stringify(removeFalseys([50, 60, 90, 100, 20,,false, undefined])) === JSON.stringify([50, 60, 90, 100, 20]), `removeFalseys first attempt!`);
console.assert(JSON.stringify(removeFalseys([null, 0, 0, 'false', false, true])) === JSON.stringify(['false', true]), `removeFalseys second attempt!`);
console.assert(JSON.stringify(removeFalseys([null, undefined, 0, '', NaN, 0n],)) === JSON.stringify([]), `removeFalseys third attempt!`);
console.assert(JSON.stringify(removeFalseys(['false', true, 'false', 'true', true])) === JSON.stringify(['false', true, 'false', 'true', true]), `removeFalseys fourth attempt!`);

console.assert(JSON.stringify(removeFalseys_1([50, 60, 90, 100, 20,,false, undefined])) === JSON.stringify([50, 60, 90, 100, 20]), `removeFalseys first attempt!`);
console.assert(JSON.stringify(removeFalseys_1([null, 0, 0, 'false', false, true])) === JSON.stringify(['false', true]), `removeFalseys second attempt!`);
console.assert(JSON.stringify(removeFalseys_1([null, undefined, 0, '', NaN, 0n],)) === JSON.stringify([]), `removeFalseys third attempt!`);
console.assert(JSON.stringify(removeFalseys_1(['false', true, 'false', 'true', true])) === JSON.stringify(['false', true, 'false', 'true', true]), `removeFalseys fourth attempt!`);

console.assert(JSON.stringify(removeFalseys_2([50, 60, 90, 100, 20,,false, undefined])) === JSON.stringify([50, 60, 90, 100, 20]), `removeFalseys first attempt!`);
console.assert(JSON.stringify(removeFalseys_2([null, 0, 0, 'false', false, true])) === JSON.stringify(['false', true]), `removeFalseys second attempt!`);
console.assert(JSON.stringify(removeFalseys_2([null, undefined, 0, '', NaN, 0n],)) === JSON.stringify([]), `removeFalseys third attempt!`);
console.assert(JSON.stringify(removeFalseys_2(['false', true, 'false', 'true', true])) === JSON.stringify(['false', true, 'false', 'true', true]), `removeFalseys fourth attempt!`);

console.assert(JSON.stringify(removeFalseys_3([50, 60, 90, 100, 20,,false, undefined])) === JSON.stringify([50, 60, 90, 100, 20]), `removeFalseys first attempt!`);
console.assert(JSON.stringify(removeFalseys_3([null, 0, 0, 'false', false, true])) === JSON.stringify(['false', true]), `removeFalseys second attempt!`);
console.assert(JSON.stringify(removeFalseys_3([null, undefined, 0, '', NaN, 0n],)) === JSON.stringify([]), `removeFalseys third attempt!`);
console.assert(JSON.stringify(removeFalseys_3(['false', true, 'false', 'true', true])) === JSON.stringify(['false', true, 'false', 'true', true]), `removeFalseys fourth attempt!`);

