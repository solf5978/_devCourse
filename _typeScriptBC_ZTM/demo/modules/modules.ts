/* eslint-disable */
import { strict as assert } from "assert";

// ES modules provide a way to organize code into separate files that can be
// imported and used in other files.To use an ES module, the the `import`
// keyword is used.
//
// Useful links:
// https://www.typescriptlang.org/docs/handbook/2/modules.html
import { add, pi, Int as Integer } from "./math.js";
// import { Point } from "./coord.js";
import Point from "./coord.js";
// You can also use import with different name when default existed
import Coordinate from "./coord.js";

const three: Integer = 3;
const four = add(2, 2);
const p1: Point = { x: 1, y: 2 };
