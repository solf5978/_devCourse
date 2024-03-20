/* eslint-disable */
import { strict as assert } from "assert";

// Useful links:
// https://www.typescriptlang.org/docs/handbook/declaration-files/templates/module-d-ts.html

import { add, setCase, quote, max } from "./mylib";
import type { CaseKinds } from "./mylib";

const message = "Hello, world!";
const upper = setCase(message, "sentence");
