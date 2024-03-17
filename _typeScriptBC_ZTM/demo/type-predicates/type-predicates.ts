/* eslint-disable */
import { strict as assert } from "assert";

// Type predicates offer a way to determine the type of data based on a
// condition. This is achieved by defining a function that takes a some data as
// an argument, applies type guards, and returns a boolean indicating whether
// the data is a specific type. The function is then used to narrow down the
// type of the variable in subsequent code. Type predicates are useful when
// dealing with union types or other situations where the type of a variable
// may not be known at compile-time. Type predicates allow the type to be
// determined correctly which avoids runtime errors.
//
// Useful links:
// https://www.typescriptlang.org/docs/handbook/2/narrowing.html#using-type-predicates

//type guard
type StrOrNum = string | number;
function sample(data: StrOrNum) {
  if (typeof data === "string") {
    console.log(data);
  } else {
    console.log(data);
  }
}
// type predicate
interface Square {
  kind: "square";
  size: number;
}

interface Circle {
  kind: "circle";
  size: number;
}

type Shape = Square | Circle;
function isSquare(shape: Shape): shape is Square {
  return shape.kind === "square";
}

function isCircle(shape: Shape): shape is Circle {
  return shape.kind === "circle";
}

function calArea(shape: Shape): number {
  if (isSquare(shape)) {
    return shape.size * shape.size;
  } else if (isCircle(shape)) {
    return Math.PI * shape.size * shape.size;
  } else {
    throw new Error("unknown shape");
  }
}
