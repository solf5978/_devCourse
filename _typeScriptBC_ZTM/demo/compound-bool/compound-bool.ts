/* eslint-disable */
import { strict as assert } from "assert";

const writing = true;
const reading = !writing;

const rating = 9;
const favouriteMovie = false;

const suggestMovie = rating > 8 || favouriteMovie;
assert.equal(suggestMovie, true);

const age = 18;
const isTeenager = age >= 13 && age < 20;
assert.equal(isTeenager, true);

const packageWeight = 30;
const packageLength = 10;
const feeExemption = false;

const extraFee = !feeExemption && (packageWeight > 25 || packageLength > 40);
