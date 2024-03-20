/* eslint-disable */
import { strict as assert } from "assert";

// Useful links:
// https://www.typescriptlang.org/docs/handbook/declaration-files/templates/module-d-ts.html

import { apiResponse } from "./mylib";

const res = apiResponse();
if (res !== undefined) {
  if (res.status === "success") {
    console.log(res.data.items[1].name);
  }
}
