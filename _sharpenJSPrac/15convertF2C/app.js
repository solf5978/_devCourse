
// Create a function that convert fahrenheit to celsius and celsius to fahrenheit. The function will accept a string that consists of a number and either C or F (32F) and return a string with the degrees using the alternative measurement (0°C). Return a rounded whole number. If something else is passed in, the function should return an error message (Error: Invalid Input).

// celsius = (F - 32) * 5/9 fahrenheit = (C * 9/5) + 32

const convertDegrees = function(str) {
    let regEx = /^-*\d{1,}°*([CFcf]|Celsius|Fahrenheit)$/;
    let degreeUnit = /[Cc]/;

    if (regEx.test(str)) {
        if (degreeUnit.test(str)) {
            return `${Math.round(parseInt(str) * (9 / 5)) + 32}°F`;
        }
        return `${Math.round((parseInt(str) - 32) * (5 / 9))}°C`;
    }
    return "Error: Invalid Input";
};


















// console.log(convertDegrees('45°F'));


// Testing convertDegrees...

console.assert((convertDegrees('95F')) === '35°C', `Convert from Fahrenheit to Celsius.`);
console.assert((convertDegrees('-12C')) === '10°F', `Convert from Celsius to Fahrenheit.`);
console.assert((convertDegrees('100°C')) === ('212°F'), `Convert from Celsius to Fahrenheit.`);
console.assert((convertDegrees('100')).includes('Error'), `Test error message.`);
console.assert((convertDegrees('10degrees')).includes('Error'), `Test error message.`);
console.assert((convertDegrees('20 Celsius')).includes('Error'), `Test error message.`);