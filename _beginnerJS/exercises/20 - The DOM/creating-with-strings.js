const item = document.querySelector('.item')

const width = 500
const src = 'dog.jpg'
const desc = `Cute Pup <img onload="alert('HACKED')" src="images/test.jpg"/>`;
const myHTML = `
  <div class="wrapper">
    <h2>Cute ${desc}</h2>
    <img src="${src}" alt="${desc}"/>
  </div>
`;

item.innerHTML = `
  <div>
    <h1> Hey How are ya? </h1>
  <div>
`

item.innerHTML = myHTML
console.log(myHTML.classList)
console.log(typeof myHTML)
console.log(item.innerHTML)
const itemImage = document.querySelector('.wrapper')
console.log(itemImage)

const myFragment = document
        .createRange()
        .createContextualFragment(myHTML)

document.body.appendChild(myFragment)