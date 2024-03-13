/* eslint-disable */

// A variable is a named memory location that can hold a value. Variables can
// be used to store a wide range of data types, such as numbers, strings, and
// arrays. A variable is declared by specifying its name, data type, and
// optionally an initial value. Once a variable is declared, it can be read
// potentially updated in other parts of the program.
//
// Useful links:
// https://www.typescriptlang.org/docs/handbook/variable-declarations.html#let-declarations

// double quotes are allowed
const courseName = "typescript";
// single quote is allow too.
const demo3 = "typescript";
// backtick style
const demo5 = `typescript`;

let demo7 = "typescript";
demo7 = "Hello" + demo7;

const amount = 100;
const fraction = 10.5;
const oneTHousand = 1e3;
const allPermissions = 0o777;

const binary = 0b0101;
const bigInt = 9000n;
const yes = true;
const no = false;
const missing = undefined;
const empty = null;

let someNum = 0;
someNum = 10;
someNum = -10;
someNum = 10.5;

// using block to scope variables

{
  let someNum = 0;
  someNum = 10;
  someNum = -10;
  someNum = 10.5;
}

// uninitialized variables
let huioo;
