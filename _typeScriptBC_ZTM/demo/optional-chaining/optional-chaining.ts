/* eslint-disable */

// Optional fields are convenient because they allow situations
// where it may not be appropriate to have data present. However,
// they make it cumbersome to access any additional data that is
// behind the optional field. For example, trying to access multiple
// optional objects one after the other requires multiple checks for
// `undefined` and multiple `if` blocks.
//
// With 'Optional Chaining', it is possible to combine all of the `if`
// blocks into a single line using the 'optional property access' operator.

// The optional property access operator is a question mark (?) and allows
// access to optional fields. It will continue to access optional fields
// using the following behavior:
//  - Access fields until `undefined` is encountered, and then set the
//    expression to `undefined.`
//  - Access fields until the last field is accessed, and then set the
//    expression to the value of the last field.
//
// Useful links:
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining

interface Pii {
  age?: number;
  addr?: string;
}

interface SearchResult {
  name: string;
  pii?: Pii;
}

class Database {
  search(name: string): SearchResult | undefined {
    switch (name) {
      case "John":
        return {
          name: "John",
          pii: {
            age: 30,
            addr: "123 Main St",
          },
        };
      case "Jane":
        return {
          name: "Jane",
        };
      default:
        return undefined;
    }
  }
}

const db = new Database();

{
  const result = db.search("John");
  if (
    result !== undefined &&
    result !== null &&
    result.name !== undefined &&
    result.pii?.addr !== undefined &&
    result.pii?.age !== null
  ) {
    console.log(result.name);
    console.log(result.pii.age);
    console.log(result.pii.addr);
  }
}

//with optional chaining
{
  const chain = db.search("John");
  if (chain?.pii?.age) {
    console.log(chain.pii.age);
  }
}
