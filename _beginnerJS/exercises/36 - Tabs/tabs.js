console.log('ya ya wes we get it.. IT WORKS!');
const tabs = document.querySelector('.tabs')
const tabButtons = tabs.querySelectorAll('[role="tab"]')
const tabPanels = Array.from(tabs.querySelectorAll('[role="tabpanel"]'))

function handleTabClick(event) {
    console.log(event.currentTarget)
    console.log(tabPanels)

    tabPanels.forEach( panel => {
        console.log(panel)
        panel.hidden = true
})

// tabButtons.forEach( tab => {
//     tab.ariaSelected = false
//     tab.setAttribute('aria-selected', false)

//     event.currentTarget.setAttribute('aria-selected', true)
//     const { id } = event.currentTarget
//     console.log(id)

//     const tabPanel = tabs.querySelector(`[aria-labelledby="${ id }"]`)
//     console.log(tabPanel)
//     tabPanel.hidden = false
// })


    console.log(tabPanels)
    const tabPanel = tabPanels.find( panel => panel.getAttribute('aria-labelledby') === id) 
    tabPanel.hidden = false;
}


tabButtons.forEach(button => button.addEventListener('click', handleTabClick))