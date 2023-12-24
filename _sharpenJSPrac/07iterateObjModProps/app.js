
// Enhance the objProps function to accept a function that will be applied to every property.

// Create a function that can be passed into objProps that will check property values for strings that are actually numbers. If so convert the value to a number.

const isObject = function(val) {
  return (typeof val === 'object' && val !== null);
};

const toNum = function(obj, key) {
  if (!isNaN(obj[key])) obj[key] = Number(obj[key])
}

const objProps = function(obj, fn) {
  for (let val in obj) {
    if (isObject(obj[val])) {
      objProps(obj[val], fn);
    } else {
      if (typeof fn === 'function') fn(obj, val)
    }
  }
};



var user = {
  firstName: "John",
  lastName: "Doe",
  email: "sdoe@allthingsjavascript.com",
  type: {
      type1: "admin",
      type2: "user"
  },
  active: 'true',
  address: {
      street: {
          street1: "100 N. Main",
          street2: "Apt. 5"
      },
      city: "Lehi",
      zip: '10001'
  },
  age: '31'
};

var quiz = {
  id: 'quiz1',
  subjPerc: {
    subj1: 20,
    subj2: 0,
    subj3: 50,
    subj4: 10,
    subj5: 20
  },
  scores: ['100', 50, 60, '70', 25, 45, '90', 85]
};

objProps(quiz, toNum);
console.dir(quiz);
console.dir(user);