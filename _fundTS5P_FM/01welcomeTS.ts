/**
 * Create  a promise that resolves after few seconds
 * @param num number of millseconds beofre promise resolves
 */

function timeout(num: number) {
  return new Promise((res) => setTimeout(res, num));
}

/**
 * Add two numbers
 * @param a first number
 * @param b second
 */

export async function addNumbers(a: number, b: number) {
  await timeout(500);
  return a + b;
}

class Foo {
  static #bar = 3;
  static getValue() {
    return Foo.#bar;
  }
}

(async () => {
  console.log(await addNumbers(Foo.getValue(), 4));
})();
