// Make a div
const div = document.createElement('div')

// add a class of wrapper to it
div.classList.add('wrapper')
// put it into the body
document.body.appendChild(div)
// make an unordered list
const ul = document.createElement('ul')
const ulHTML = `<ul>
 <li>one</li>
 <li>two/li>
 <li>three</li>
 </ul>`

// add three list items with the words "one, two three" in them
ul.innerHTML = ulHTML
// put that list into the above wrapper
div.appendChild(ul)
// create an image
const img = document.createElement('img')
// set the source to an image
img.src = "images/hello.jpg"
// set the width to 250
img.width = 250
// add a class of cute
img.classList.add('cute')
// add an alt of Cute Puppy
img.alt = 'Cute Puppy'
// Append that image to the wrapper
div.appendChild(img)
// with HTML string, make a div, with two paragraphs inside of it
// put this div before the unordered list from above
const div2P = `
<div>
  <p>Paragraph 1</p>
  <p>Paragraph 2</p>
</div>`
const ulElement = div.querySelector('ul')
ulElement.insertAdjacentHTML('beforebegin', div2P)
// add a class to the second paragraph called warning
const myDiv = div.querySelector('div p')
myDiv.children[1].classList.add('class-p')
myDiv.firstElementChild.remove()
// remove the first paragraph

// create a function called generatePlayerCard that takes in three arguments: name, age, and height
function generatePlayerCard(name, age, height) {
   return (
   `<div class="playerCard">
    <h2>{name} - {age}</h2>
    <p>They are {height} and {age} years old. In Dog years this person would be {age * 7}. That would be a tall dog!</p>
    <button type="button"> &times; </button>
    </div>`
   )
}
// have that function return html that looks like this:
// <div class="playerCard">
//   <h2>NAME — AGE</h2>
//   <p>They are HEIGHT and AGE years old. In Dog years this person would be AGEINDOGYEARS. That would be a tall dog!</p>
// </div>

// make a new div with a class of cards
const cards = document.createElement('div')
cards.classList.add('card')


// Have that function make 4 cards
let cardsHTML = generatePlayerCard('wes', 12, 150);
cardsHTML += generatePlayerCard('scott', 12, 150);
cardsHTML += generatePlayerCard('kait', 12, 150);
cardsHTML += generatePlayerCard('snickers', 12, 150);


// append those cards to the div
cards.insertAdjacentHTML('afterbegin', cardsHTML)

// put the div into the DOM just before the wrapper element

document.querySelector('.wrapper').appendChild(cards)
// Bonus, put a delete Button on each card so when you click it, the whole card is removed
const buttons = document.querySelectorAll('.delete');
// make out delete function
function deleteCard(event) {
  const buttonThatGotClicked = event.currentTarget;
  // buttonThatGotClicked.parentElement.remove();
  buttonThatGotClicked.closest('.playerCard').remove();
}
// loop over them and attach a listener
buttons.forEach(button => button.addEventListener('click', deleteCard));
