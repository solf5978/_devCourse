
const countTruthys = function(arry) {
  let tot = 0;
  for (let elem of arry) {
    if (elem) tot++;
    //tot += elem;
  };
  return tot;
};

const countTruthys_1 = function(arry) {
  let tot = 0;
  arry.forEach((elem) => {
    if (elem) tot++
  });
  return tot;
};

const countTruthys_2 = function(arry) {
  let truesArray = arry.filter((elem) => elem);
  return truesArray.length;
};

const countTruthys_3 = function(arry) {
  return arry.reduce((acc, elem) => {
    if (elem) {
      return acc + 1;
    } else {
      return acc;
    }
  }, 0);
};

const countTruthys_4 = function(arry) {
  return arry.reduce((acc, elem) => elem ? acc + 1: acc , 0);
};













// Testing countTruthys...

console.assert(countTruthys([1, 1, 'true', true, 'true', true]) === 6, `countTruthys first attempt!`);
console.assert(countTruthys([undefined, null, 0, 0, false, false, true]) === 1, `countTruthys second attempt!`);
console.assert(countTruthys([]) === 0, `countTruthys third attempt!`);
console.assert(countTruthys([false, true, false, true, true]) === 3, `countTruthys fourth attempt!`);
console.assert(countTruthys([false]) === 0, `countTruthys fifth attempt!`);

console.assert(countTruthys_1([1, 1, 'true', true, 'true', true]) === 6, `countTruthys first attempt!`);
console.assert(countTruthys_1([undefined, null, 0, 0, false, false, true]) === 1, `countTruthys second attempt!`);
console.assert(countTruthys_1([]) === 0, `countTruthys third attempt!`);
console.assert(countTruthys_1([false, true, false, true, true]) === 3, `countTruthys fourth attempt!`);
console.assert(countTruthys_1([false]) === 0, `countTruthys fifth attempt!`);

console.assert(countTruthys_2([1, 1, 'true', true, 'true', true]) === 6, `countTruthys first attempt!`);
console.assert(countTruthys_2([undefined, null, 0, 0, false, false, true]) === 1, `countTruthys second attempt!`);
console.assert(countTruthys_2([]) === 0, `countTruthys third attempt!`);
console.assert(countTruthys_2([false, true, false, true, true]) === 3, `countTruthys fourth attempt!`);
console.assert(countTruthys_2([false]) === 0, `countTruthys fifth attempt!`);

console.assert(countTruthys_3([1, 1, 'true', true, 'true', true]) === 6, `countTruthys first attempt!`);
console.assert(countTruthys_3([undefined, null, 0, 0, false, false, true]) === 1, `countTruthys second attempt!`);
console.assert(countTruthys_3([]) === 0, `countTruthys third attempt!`);
console.assert(countTruthys_3([false, true, false, true, true]) === 3, `countTruthys fourth attempt!`);
console.assert(countTruthys_3([false]) === 0, `countTruthys fifth attempt!`);

console.assert(countTruthys_4([1, 1, 'true', true, 'true', true]) === 6, `countTruthys first attempt!`);
console.assert(countTruthys_4([undefined, null, 0, 0, false, false, true]) === 1, `countTruthys second attempt!`);
console.assert(countTruthys_4([]) === 0, `countTruthys third attempt!`);
console.assert(countTruthys_4([false, true, false, true, true]) === 3, `countTruthys fourth attempt!`);
console.assert(countTruthys_4([false]) === 0, `countTruthys fifth attempt!`);
