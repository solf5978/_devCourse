'use strict';

const removeFalseys = function(arry) {
  
};















// Testing removeFalseys...

console.assert(JSON.stringify(removeFalseys([50, 60, 90, 100, 20,,false, undefined])) === JSON.stringify([50, 60, 90, 100, 20]), `removeFalseys first attempt!`);
console.assert(JSON.stringify(removeFalseys([null, 0, 0, 'false', false, true])) === JSON.stringify(['false', true]), `removeFalseys second attempt!`);
console.assert(JSON.stringify(removeFalseys([null, undefined, 0, '', NaN, 0n],)) === JSON.stringify([]), `removeFalseys third attempt!`);
console.assert(JSON.stringify(removeFalseys(['false', true, 'false', 'true', true])) === JSON.stringify(['false', true, 'false', 'true', true]), `removeFalseys fourth attempt!`);

