/* eslint-disable */

// Exceptions are a way to handle errors and unexpected behavior in your code.
// When an exception occurs, it interrupts the normal flow of the program and
// jumps to a predefined error-handling routine. Exceptions can be used to
// catch and handle errors in a way that doesn't crash the program or cause
// unexpected behavior. Exceptions are thrown using the `throw` keyword and
// caught using the `try...catch` statement.
//
// Useful links:
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch

function divide(lhr: number, rhs: number): number {
  if (rhs === 0) {
    throw new Error("Cannot divide by 0");
  } else if (rhs === 1) {
    return lhr;
  } else {
    return lhr / rhs;
  }
}

try {
  const b = divide(100, 0);
  console.log(b);
} catch (e) {
  console.log(`Errir -> ${e}`);
} finally {
  console.log("Finally");
}
