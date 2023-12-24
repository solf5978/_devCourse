
// Create a function that returns the frequency distribution of an array. This function should return an object, where the keys are the unique elements and the values are the frequency in which those elements occur.

const getFrequencyObj = function(arr) {
    let obj = {};
    for (let _ = 0; _ < arr.length; _++) {
        let elem = arr[_];
        if (obj[elem]) {
            obj[elem] = obj[elem] + 1;
        } else {
            obj[elem] = 1;
        }
    }
    return obj;  
}

const getFrequencyObj_1 = function(arr) {
    let obj = {};

    for (let idx = 0; idx < arr.length; idx++) {
        let elem = arr[idx];
        obj[elem] = obj[elem] ? obj[elem] + 1 : 1;
    }
    return obj;
}

const getFrequencyObj_2 = function(arr) {
    return arr.reduce((acc, elem) => {
        acc[elem] = (acc[elem] || 0) + 1;
        return acc;
    }, {});
}

















//console.log(getFrequencyObj(['a','b','A','A','a','a','C','a','d']));
//console.log(getFrequencyObj([1,1,1,2,3,4,5,5,6,2,2,2]));
//console.log(getFrequencyObj([]));


// Testing getFrequencyObj...

console.assert(JSON.stringify(getFrequencyObj(['a','b','A','A','a','a','C','a','d'])) === JSON.stringify({a:4,b:1,A:2,C:1,d:1}), `Get frequency object for an array of letters.`);
console.assert(JSON.stringify(getFrequencyObj([1,1,1,2,3,4,5,5,6,2,2,2])) === JSON.stringify({'1':3,'2':4,'3':1,'4':1,'5':2,'6':1,}), `Get frequency object for an array of numbers.`);
console.assert(JSON.stringify(getFrequencyObj([])) === JSON.stringify({}), `Get frequency object for an empty array.`);

console.assert(JSON.stringify(getFrequencyObj_1(['a','b','A','A','a','a','C','a','d'])) === JSON.stringify({a:4,b:1,A:2,C:1,d:1}), `Get frequency object for an array of letters.`);
console.assert(JSON.stringify(getFrequencyObj_1([1,1,1,2,3,4,5,5,6,2,2,2])) === JSON.stringify({'1':3,'2':4,'3':1,'4':1,'5':2,'6':1,}), `Get frequency object for an array of numbers.`);
console.assert(JSON.stringify(getFrequencyObj_1([])) === JSON.stringify({}), `Get frequency object for an empty array.`);

console.assert(JSON.stringify(getFrequencyObj_2(['a','b','A','A','a','a','C','a','d'])) === JSON.stringify({a:4,b:1,A:2,C:1,d:1}), `Get frequency object for an array of letters.`);
console.assert(JSON.stringify(getFrequencyObj_2([1,1,1,2,3,4,5,5,6,2,2,2])) === JSON.stringify({'1':3,'2':4,'3':1,'4':1,'5':2,'6':1,}), `Get frequency object for an array of numbers.`);
console.assert(JSON.stringify(getFrequencyObj_2([])) === JSON.stringify({}), `Get frequency object for an empty array.`);