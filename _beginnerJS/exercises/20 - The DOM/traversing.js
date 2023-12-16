const first = document.querySelector('.wes')

console.log(first.children)
console.log(first.childNodes)
console.log(first.firstElementChild)
console.log(first.lastElementChild)
console.log(first.previousElementSibling)
console.log(first.nextElementSibling)
console.log(first.parentElement)

const p = document.createElement('p')
p.textContent = "Gonna be removed node"
document.body.appendChild(p)

p.remove()
console.log(p)