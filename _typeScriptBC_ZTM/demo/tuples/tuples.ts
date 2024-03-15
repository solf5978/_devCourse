/* eslint-disable */
import { strict as assert } from "assert";

// Tuples provide a way to express an array with a fixed number of elements of
// different types, creating a data structure with multiple different types.
// They can be especially handy when dealing with scenarios such as
// representing coordinates, storing key-value pairs, or returning multiple
// values from a function. Since they are type-checked, TypeScript can ensure
// that the values in the tuple are correct at compile time.
//
// Useful links:
// https://www.typescriptlang.org/docs/handbook/2/objects.html#tuple-types

type Title = string;
type Publishyear = number;

type Book = [Title, Publishyear];

const sample: Book = ["The Hitchhiker's Guide to the Galaxy", 1999];
const animalFarm: Book = ["Animal Farm", 2000];
const mistBorn: Book = ["mistborn", 2000];

function coord(): [number, number] {
  return [100, 50];
}

const coordinates = coord();
assert(coordinates[0] === 100 && coordinates[1] === 50);
