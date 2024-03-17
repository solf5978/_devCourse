/* eslint-disable */
import { strict as assert } from "assert";

// Type assertions allow you to tell the compiler that a value should be
// considered a certain type, even if TypeScript cannot infer the type
// automatically. You can use type assertions to help the compiler recognize
// the types of variables, function return types, and more. When using type
// assertions, be sure to only assert types that are actually correct, as
// asserting an incorrect type can lead to runtime errors in your code.
//
// Useful links:
// https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-assertions

const greet: unknown = "Hello";
const hello = greet as string;

const numChars = (greet as string).length;

interface Employee {
  position(): string;
}

class Manager implements Employee {
  position(): string {
    return "Manager";
  }
  greet(): void {
    console.log(hello);
  }
}

const alice: Employee = new Manager();
alice.position();
