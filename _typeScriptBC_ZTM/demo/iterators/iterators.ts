/* eslint-disable */

// Iterators offer a way to traverse the elements of a collection one by one.
// The purpose of iterators is to provide a standard way for accessing and
// iterating over collections, such as arrays or maps, in a language-agnostic
// way. Using iterators, you can iterate over collections in a loop without
// having to worry about the underlying implementation of the collection.
//
// Useful links:
// https://www.typescriptlang.org/docs/handbook/iterators-and-generators.html

const demoArray = [1, 2, 3, 4, 5, 6];

for (let i = 0; i < demoArray.length; i++) {
  console.log(demoArray[i]);
}

for (const value of demoArray) {
  console.log(value);
}

const nums = {
  one: 1,
  two: 2,
  three: 3,
  four: 4,
  five: 5,
  six: 6,
};

let property: keyof typeof nums;

for (property in nums) {
  console.log(property);
  console.log(nums[property]);
}
