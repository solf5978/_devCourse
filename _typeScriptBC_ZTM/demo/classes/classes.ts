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
  //   height: number;
  length: number;

  constructor(width: number, public height: number, length: number) {
    this.width = width;
    this.height = height;
    this.length = length;
  }
}

const one = new Dimensions(1, 1, 1);

class Point {
  constructor(public x: number, public y: number) {
    this.x = x;
    this.y = y;
  }

  translate(dx: number, dy: number): Point {
    return new Point(this.x + dx, this.y + dy);
  }
}

const p1 = new Point(1, 1);
p1.translate(15, 15);
