
// Create a function that inserts a white space before every upper-case character that exists in a string.

/* const insertWhiteSpace = function(str) {
  let regEx = /[A-Z]/g;

  let strArr = [...str].map((elem, idx) => regEx.test(elem) && idx !== 0 ? ' ' + elem : elem);
  return strArr.join('');
}; */

const insertWhiteSpace = function(str) {
  //return str.replace(/([A-Z])/g," $1");
  return str.replace(/(?<=[a-z])([A-Z])/g," $1");
};


















console.log(insertWhiteSpace('RunAsFastAsYouCan'));


// Testing insertWhiteSpace...

console.assert((insertWhiteSpace('How many times?At least 10.')) === 'How many times? At least 10.', `Insert space after punctuation.`);
console.assert((insertWhiteSpace('RunAsFastAsYouCan.')) === 'Run As Fast As You Can.', `Insert space between each word.`);
console.assert((insertWhiteSpace('runasfastasyoucan.')) === ('runasfastasyoucan.'), `No uppercase letters.`);