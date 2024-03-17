/* eslint-disable */

// Union types allows you to declare a variable or parameter that can hold
// multiple types of value and are declared using the pipe symbol (|) between
// the types. Union types can be useful when you want something to accept
// multiple types of input.
//
// Useful links:
// https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#union-types

type Color = "red" | "green" | "blue";

const r: Color = "red";
const g: Color = "green";
const b: Color = "blue";

function setBgColor(color: Color): void {
  switch (color) {
    case "red":
      document.body.style.backgroundColor = "red";
      break;
    case "green":
      document.body.style.backgroundColor = "green";
      break;
    case "blue":
      document.body.style.backgroundColor = "blue";
      break;
  }
}
