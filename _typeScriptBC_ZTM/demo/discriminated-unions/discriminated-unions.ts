/* eslint-disable */

// Discriminated unions are a way to declare a type that can have
// different properties or behaviors based on a specific discriminator property.
// Discriminated unions can be defined using the intersection of a set of types
// with a common property, and the property value can be used to determine which
// type to use.

// We can also use entire objects. Using objects creates
// a 'discriminated union'. Unions only allow the type to be one
// option at a time. Combining this with objects allows multiple
// pieces of data to be associated with each individual option.

type numbers = 1 | 2 | 3 | number;
type AccountCreationMessage =
  | { kind: "ok"; greeting: string }
  | { kind: "passwordComplexityFailure"; message: string }
  | { kind: "usernameExists" };

const ok: AccountCreationMessage = { kind: "ok", greeting: "Hello, world!" };
const passwordTooShort: AccountCreationMessage = {
  kind: "passwordComplexityFailure",
  message: "Password must be at least 8 characters long",
};

function showMessage(msg: AccountCreationMessage) {
  switch (msg.kind) {
    case "ok":
      console.log(msg.greeting);
      break;
    case "passwordComplexityFailure":
      console.log(msg.message);
      break;
    case "usernameExists":
      console.log(msg);
      break;
    default:
      break;
  }
}

showMessage(ok);
showMessage(passwordTooShort);
showMessage({ kind: "usernameExists" });
