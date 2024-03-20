/* eslint-disable */
import { strict as assert } from "assert";

// Useful links:
// https://www.typescriptlang.org/docs/handbook/iterators-and-generators.html

function* genValues(): Generator<number> {
  yield 1;
  yield 2;
  yield 3;
  yield 4;
  yield 5;
}

const values = genValues();
assert.equal(values.next().value, 1);
assert.equal(values.next().value, 2);
assert.equal(values.next().value, 3);
assert.equal(values.next().value, undefined);

class Range implements Iterable<number> {
  private readonly start: number;
  private readonly end: number;

  constructor(start: number, end: number) {
    this.start = start;
    this.end = end;
  }

  *[Symbol.iterator](): Generator<number> {
    for (let i = this.start; i <= this.end; i++) {
      yield i;
    }
  }
}

const range = new Range(1, 5);
for (const value of range) {
  console.log(value);
}
