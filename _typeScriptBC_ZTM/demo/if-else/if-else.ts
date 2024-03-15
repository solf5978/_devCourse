/* eslint-disable */
import { strict as assert } from "assert";

// Control flow is the order in which statements are executed in a program. It
// allows programmers to control the flow of their code based on certain
// conditions or events. Control flow structures include conditional
// statements, loops, and function calls, which allow for branching and
// repetition of code.
//
// Useful links:
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else

const answer = 42;

if (answer === 42) {
  console.log("Correct!");
} else {
  console.log("Wrong!");
}

if (answer === 42) {
  console.log("Correct!");
} else if (answer === 43) {
  console.log(`answer is {answer}`);
} else {
  console.log("Wrong!");
}

const hasTheSkill = true;
const isTuesday = true;
const totalOvertime = 0.5;
const holidaySeason = false;

function approveWork() {
  if (hasTheSkill && (isTuesday || (holidaySeason && totalOvertime > 0.5))) {
    console.log("Approved!");
  } else {
  }
}

function hasOvertimeHours(hoursWorked: number, totalOvertime: number): boolean {
  return hoursWorked > totalOvertime;
}
