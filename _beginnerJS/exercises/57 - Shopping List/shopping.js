const shoppingForm = document.querySelector('.shopping')
const list = document.querySelector('.list')

let items = []

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
        <input 
        type='checkbox'
        ${item.completed && 'checked'}
        value="${item.id}>
        <span class='itemName'>${item.name}</span>
        <button 
        aria-label="Remove ${item.name}"
        value="${item.id}"
        >&times;</button>
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
    const newItems = item.filter(item => item.id !== id)
    items = newItems
    list.dispatchEvent(new CustomEvent('itemsUpdated'))
}

function markAsComplete(id) {
    console.info('hi', id)
    const itemRef = items.find(item => item.id === id)
    console.info('get the ref', itemRef)
    itemRef.complete = !itemRef.complete
    list.dispatchEvent(new CustomEvent('itemsUpdated'))
}

shoppingForm.addEventListener('submit', handleSubmit)
list.addEventListener('itemsUpdated', displayItems)
list.addEventListener('itemsUpdated', mirrorToLocalStroage)
list.addEventListener('click', function(e) {
    if(e.target.matches('button')) {
        deleteItem(parseInt(e.target.value))
    }
    if(e.target.matches('input[type="checkbox"[')) {
        markAsComplete(parseInt(e.target.value))
    }
})
restoreFromLocalStorage()

// const buttons = list.querySelectorAll('button')
// buttons.forEach(button => button.addEventListener('click', deleteItem))

