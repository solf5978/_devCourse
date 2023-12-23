
const countTheTrues = function(arry) {
    let boolCount = 0;
    for (let arr of arry) {
        if (arr != 0) {
            boolCount++;
        };
    }
    return boolCount;
};

// Alternative Using The True Nature of True/False
const countTheTrues_1 = function(arry) {
    let boolCount = 0;
    for (let arr of arry) {
        boolCount = boolCount + arr;
    }
    return boolCount;
}

// Solution 2 Using forEach + CallBack
const countTheTrues_2 = function(arry) {
    let boolCount = 0;
    arry.forEach((arr) => boolCount += arr);
    return boolCount;
}

// Solution 3 Using Filter To Pass In Only True Array
const countTheTrues_3 = function(arry) {
    let truesArray = arry.filter((arr) => arr);
    return truesArray.length;
}

// Solution 4 Using Reduce
const countTheTrues_4 = function(arry) {
    return arry.reduce((prevVal, currVal) => prevVal + currVal, 0);
}












// Testing countTheTrues...

console.assert(countTheTrues([true, true, true, true, true, true]) === 6, `countTheTrues first attempt!`);
console.assert(countTheTrues([false, false, false, false, false, false, true]) === 1, `countTheTrues second attempt!`);
console.assert(countTheTrues([]) === 0, `countTheTrues third attempt!`);
console.assert(countTheTrues([false, true, false, true, true]) === 3, `countTheTrues fourth attempt!`);
console.assert(countTheTrues([false]) === 0, `countTheTrues fifth attempt!`);

console.assert(countTheTrues_1([true, true, true, true, true, true]) === 6, `countTheTrues first attempt!`);
console.assert(countTheTrues_1([false, false, false, false, false, false, true]) === 1, `countTheTrues second attempt!`);
console.assert(countTheTrues_1([]) === 0, `countTheTrues third attempt!`);
console.assert(countTheTrues_1([false, true, false, true, true]) === 3, `countTheTrues fourth attempt!`);
console.assert(countTheTrues_1([false]) === 0, `countTheTrues fifth attempt!`);

console.assert(countTheTrues_2([true, true, true, true, true, true]) === 6, `countTheTrues first attempt!`);
console.assert(countTheTrues_2([false, false, false, false, false, false, true]) === 1, `countTheTrues second attempt!`);
console.assert(countTheTrues_2([]) === 0, `countTheTrues third attempt!`);
console.assert(countTheTrues_2([false, true, false, true, true]) === 3, `countTheTrues fourth attempt!`);
console.assert(countTheTrues_2([false]) === 0, `countTheTrues fifth attempt!`);
 
console.assert(countTheTrues_3([true, true, true, true, true, true]) === 6, `countTheTrues first attempt!`);
console.assert(countTheTrues_3([false, false, false, false, false, false, true]) === 1, `countTheTrues second attempt!`);
console.assert(countTheTrues_3([]) === 0, `countTheTrues third attempt!`);
console.assert(countTheTrues_3([false, true, false, true, true]) === 3, `countTheTrues fourth attempt!`);
console.assert(countTheTrues_3([false]) === 0, `countTheTrues fifth attempt!`);
 
console.assert(countTheTrues_4([true, true, true, true, true, true]) === 6, `countTheTrues first attempt!`);
console.assert(countTheTrues_4([false, false, false, false, false, false, true]) === 1, `countTheTrues second attempt!`);
console.assert(countTheTrues_4([]) === 0, `countTheTrues third attempt!`);
console.assert(countTheTrues_4([false, true, false, true, true]) === 3, `countTheTrues fourth attempt!`);
console.assert(countTheTrues_4([false]) === 0, `countTheTrues fifth attempt!`);
 