const p = document.querySelector(`p`)
const divs = document.querySelectorAll(`div`)
const divItem = document.querySelectorAll(`.item`)
const itemImg = document.querySelectorAll(`.item img`)
const firstItem = document.querySelector(`.item`)
const heading =document.querySelector(`h2`)
heading.textContent = `this is cool`

console.log(p)
console.log(divs)[1]
console.log(divItem)
console.log(itemImg)
console.dir(heading)
console.log(heading.textContent)
console.log(heading.innerText)
console.log(heading.innerHTML)
console.log(heading.outerHTML)

const pizzaList = document.querySelector(`.pizza`)
console.log(pizzaList.textContent)

pizzaList.textContent = `${pizzaList.textContent}🍕`
pizzaList.insertAdjacentText("afterbegin", `🍕`)
pizzaList.insertAdjacentText("beforebegin", `🍕`)

const pic = document.querySelector(`.nice`)
console.log(pic.classList)
pic.classList.add(`open`)
pic.classList.remove(`cool`)
pic.classList.add(`round`)
pic.classList.toggle(`round`)

function toggleRound() {
    pic.classList.toggle(`round`)
}
pic.addEventListener(`click`, toggleRound)
pic.alt = `cute pup`
pic.width = 200

pic.addEventListener(`load`, () => {
    console.log(pic.naturalWidth);
})

pic.setAttribute(`alt`, `really cute pup`)
console.log(pic.getAttribute(`alt`))

const custom = document.querySelector(`.custom`)
console.log(custom.dataset);
custom.addEventListener(`click`, () => {
    alert(`welcome ${custom.dataset.name} ${custom.dataset.last}`)
})