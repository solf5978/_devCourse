console.log(`it works!`)

const myParagraph = document.createElement(`p`)
myParagraph.textContent = `I am a P`
myParagraph.classList.add(`special`)
console.log(myParagraph)

const myImage = document.createElement(`img`)
myImage.src = 'https://example.cc'
myImage.alt = `nice one`

const myDiv = document.createElement(`img`)
myDiv.classList.add(`wrapper`)
console.log(myDiv)

const body = document.body.appendChild(myParagraph);
document.body.appendChild(myDiv)
myDiv.appendChild(myParagraph)
myDiv.appendChild(myImage)

const heading = document.createElement('h2')
heading.textContent = 'cool things'
myDiv.appendChild(heading)
myDiv.insertAdjacentElement('afterbegin', heading)

const uList = document.createElement('ul')
uList.appendChild('li').textContent('One')
uList.appendChild('li').textContent('Two')
uList.appendChild('li').textContent('Three')