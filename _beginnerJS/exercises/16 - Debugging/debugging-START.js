const people = [
  { name: 'Wes', cool: true, country: 'Canada' },
  { name: 'Scott', cool: true, country: 'Merica' },
  { name: 'Snickers', cool: false, country: 'Dog Country' },
];

people.forEach((person, index) => {
  console.log(person.name);
});

// Console Methods
const erroMethod = () => {
  console.info(`LightWhite Mark`)
  console.error(`Red Flag Error`)
  console.warn(`Yellow Warnning`)
  console.log(`Common Logging`)
  console.table(`Accept List/Array/Object to format as a Table`)
  console.count(`Counting/Time: `)
  console.group(`Pair with groupend`)
  console.groupCollapsed(`pair with groupend, be collapsable`)
  console.groupEnd(`Get for a group of message`)
}
// Callstack StackTracing
function first() {       // Called by Main/App
  const second = () => { // Called by first
    return (
      Map = () => {      // Called by second
        return "Hello"
      }
    )
  }
}

// Grabbing Elements
const p = `$('p')`
const o = `$$('p')`
const f12 = `Grabbing Element via F12, then with ${0, 1, 2, 3} elements`
const consoleOnly = `$ only works in console without JQuery`

// Breakpoints

function running(para1) {
  debugger; // adding breakpoint
  console.log(`halt`)
  debugger;
  console.log(`another halt`)
}

// Scope

// Network Requests

// Break On Attribute

// Some Setup Code

function doctorize(name) {
  return `Dr. ${name}`;
}

function greet(name) {
  doesntExist();
  return `Hello ${name}`;
}

function go() {
  const name = doctorize(greet('Wes'));
  console.log(name);
}

const button = document.querySelector('.bigger');
button.addEventListener('click', function(e) {
  const newFontSize =
    parseFloat(getComputedStyle(e.currentTarget).fontSize) + 1;
  e.currentTarget.style.fontSize = `${newFontSize}px`;
});

// A Dad joke fetch
async function fetchDadJoke() {
  const res = await fetch('https://icanhazdadjoke.com/', {
    headers: {
      Accept: 'text/plain',
    },
  });
  const joke = await res.text();
  console.log(joke);
  return joke;
}
