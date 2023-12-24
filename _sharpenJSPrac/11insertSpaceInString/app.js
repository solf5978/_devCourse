
// Create a function that inserts a white space before every upper-case character that exists in a string.

const insertWhiteSpace = function(str) {
  
};


















// console.log(insertWhiteSpace('RunAsFastAsYouCan'));


// Testing insertWhiteSpace...

console.assert((insertWhiteSpace('How many times?At least 10.')) === ' How many times? At least 10.', `Insert space after punctuation.`);
console.assert((insertWhiteSpace('RunAsFastAsYouCan.')) === ' Run As Fast As You Can.', `Insert space between each word.`);
console.assert((insertWhiteSpace('runasfastasyoucan.')) === ('runasfastasyoucan.'), `No uppercase letters.`);