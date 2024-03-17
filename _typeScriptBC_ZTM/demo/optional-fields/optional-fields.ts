/* eslint-disable */

// You can define optional fields in your object types. Optional fields are
// fields that may or may not be present in an object. You can make a field
// optional by appending a question mark "?" to its name in the type
// definition. This is useful when you have an object with some properties that
// are not always required.
//
// Useful links:
// https://www.typescriptlang.org/docs/handbook/2/objects.html#optional-properties

type Warranty = "standard" | "extended";

function warrantyInfo(warranty: Warranty | undefined): String {
  switch (warranty) {
    case "standard":
      return "Standard warranty";
    case "extended":
      return "Extended warranty";
    default:
      return "No warranty";
  }
}

interface LineItem {
  name: string;
  quantity: number;
  warranty?: Warranty | undefined;
}

function presentLineItem(lineItem: LineItem): void {
  console.log(
    `${lineItem.quantity} ${lineItem.name} ${warrantyInfo(lineItem.warranty)}`
  );
  console.log(lineItem.warranty);
  if (lineItem.warranty !== undefined) {
    console.log(warrantyInfo(lineItem.warranty));
  } else {
    console.log("No warranty");
  }
}

const boxFan: LineItem = {
  name: "Box Fan",
  quantity: 1,
};

const heater: LineItem = {
  name: "Heater",
  quantity: 1,
  warranty: "standard",
};
