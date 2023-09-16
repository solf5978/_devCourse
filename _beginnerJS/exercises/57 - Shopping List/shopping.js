const shoppingForm = document.querySelector('.shopping')
const list = document.querySelector('.list')

const items = []

function handleSubmit(e) {
    e.preventDefault()
    const name = e.currentTarget.item.value
    if (!name) return;
    const item = {
        name,
        id: Date.now(),
        complete: false,
    }

    items.push(item)
    //e.currentTarget.item.value = ''
    e.target.reset()
    //displayItems()

    //sendDataToServerAboutUpdatedItems()
    list.dispatchEvent(new CustomEvent('itemsUpdated'))

}

function displayItems() {
    const html = items.map( item => 
        `<li class='shopping-item">
        <input type='checkbox'>
        <span class='itemName'>${item.name}</span>
        <button aria-label="Remove $item.name}">&times;</button>
        </li>`)
        .join('')
    list.innerHTML = html
}

function mirrorToLocalStroage() {
    localStorage.setItem('items', JSON.stringify(items))
}

function restoreFromLocalStorage() {
    const lsItems = JSON.parse(localStorage.getItem('items'))
    //items.forEach(item  => items.push(item))
    items.push(...lsItems)
    list.dispatchEvent(new CustomEvent('itemsUpdated'))
}

function deleteItem(id) {
    console.info('hi')
}


shoppingForm.addEventListener('submit', handleSubmit)
list.addEventListener('itemsUpdated', displayItems)
list.addEventListener('itemsUpdated', mirrorToLocalStroage)
list.addEventListener('click', function(e) {
    console.log(e.target, e.currentTarget)
})
restoreFromLocalStorage()

// const buttons = list.querySelectorAll('button')
// buttons.forEach(button => button.addEventListener('click', deleteItem))