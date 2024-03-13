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
