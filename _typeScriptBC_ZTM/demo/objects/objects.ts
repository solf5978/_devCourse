/* eslint-disable */
import { strict as assert } from "assert";

// Objects are a fundamental data type used to represent a collection of
// properties with their respective values. They are defined using either an
// object literal notation or a constructor notation.
//
// Useful links:
// https://www.typescriptlang.org/docs/handbook/2/objects.html

type Personal = String;
type employee = {
  name: Personal;
  age: Number;
  job: String;
};

function createEmployee(name: Personal, age: Number, job: String): employee {
  return {
    name: name,
    age: age,
    job: job,
  };
}

let myStuff = createEmployee("John", 30, "Software Engineer");
console.log(myStuff.name);
