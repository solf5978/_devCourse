/* eslint-disable */
import { strict as assert } from "assert";

// Classes are a way to define blueprints for objects. They encapsulate data
// and behavior and can be used to create instances of objects with predefined
// properties and methods. Classes can be extended and inherited, allowing for
// the creation of complex object hierarchies.
//
// Useful links:
// https://www.typescriptlang.org/docs/handbook/2/classes.html

class Color {
  r: number = 0;
  g: number = 0;
  b: number = 0;
}

const red = new Color();
red.r = 255;
const redValue = red.r;

class Dimensions {
  width: number;
  height: number;
  length: number;

  constructor(width: number, height: number, length: number) {
    this.width = width;
    this.height = height;
    this.length = length;
  }
}
