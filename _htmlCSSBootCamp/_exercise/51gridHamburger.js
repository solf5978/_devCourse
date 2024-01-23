const hamburgerBTN = document.querySelector(".hamburger")

const topBar = document.querySelector(".barTOP")
const midBar = document.querySelector(".barMID")
const btmBar = document.querySelector(".barBTM")

hamburgerBTN.addEventListener("click", () => {
    topBar.classList.toggle("animateTOPBar")
    midBar.classList.toggle("animateMIDBar")
    btmBar.classList.toggle("animateBTMBar")
})