/* eslint-disable */
import { strict as assert } from "assert";

// Incrementing numbers is a common task to perform when writing programs. So
// common that there is an operator dedicated to just incrementing numbers.
// However, it does come with a few caveats to be aware of.

// Useful links:
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Increment

let n = 1;
n++;
assert.strictEqual(n, 2);

++n;
assert.strictEqual(n, 3);
n = 5;
const k = n++;
assert.strictEqual(k, 5);
assert.strictEqual(n, 6);

const j = ++n;
assert.strictEqual(j, 7);
assert.strictEqual(n, 8);

n = 5;
const t = --n;
assert.strictEqual(t, 4);
assert.strictEqual(n, 4);

assert.strictEqual((n += 5), 9);
