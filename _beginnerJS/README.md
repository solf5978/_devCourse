# Course Note

## External Material
- [ESLint For Linter](https://eslint.org/)
- [Prettier For Beautify The Code](https://prettier.io/)

## Function Scoped
`var first = "live as long as the called function";`

## Block Scoped
```
let second = 300;
let third = true;
const fourth = "another";
```

## Global Scoped
```
var globalvariable = `hi`;
var globalSameAsWindow = `uptowindowscale`
```

## Function Declaration
```
// Regular Function
function regularFunction(parameter1, parameter2){
    return ``
}
// Anonymous Function
function (para1) { return `${para1} + 2`}
// Callback Function
// Something Will Run When Something Happens
const cbk = document.querySelector("Click Me");
cbk.addEventListener('click', CALLBACK_FUNCTION)
// Anonymous on Callback
cbk.addEventListener('click', function() {
    return ``
})
// Timer Callback
setTimeout(function() {
    return ``
}, 1000)
// Arrow On It
setTimeout(() => {
    return ``
}, 1000)

// Arrow Function
const anon = () => `return value here`
const anon2 = (para1, para2=2) => para1 * para2
const returnObj = (first, last) => ({ name: `${first} ${last}`, age: 0})
// Immediately Invoked Function Expression
// Using TWO Parentnesses
(function() {
    return ``
})();
// Methods
// Function Inside An Object
const obj = {
    method: function() {
        return ``
    }
    // Short-Hand Way
    method() {
        return ``
    }
    // Arrow Function
    arrow: () => {
        return ``
    }
}

expression = function expressionFunction(parameter1, parameter2){
    return ``
}
```

## CamelCase
`const andYouHoldingMe = true;`

## UpperCamelCase
`const UsuallyForFunction = false;`

## snake_case
`const often_use_in_python = true;`

## kebab-case
`const error-in-javascript = false;`