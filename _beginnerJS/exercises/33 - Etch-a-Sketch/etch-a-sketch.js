// Select the elements [canvas, shake, button]

const canvas = document.querySelector('#etch-a-sketch')
const ctx = canvas.getContext('2d')
const shakeButton = document.querySelector('.shake')
const MOVE_AMOUNT = 50

// Setup our canvas for drawing

const { width, height } = canvas
let x = Math.floor(Math.random() * width);
let y = Math.floor(Math.random() * height);

ctx.lineJoin = 'round'
ctx.lineCap = 'round'
ctx.lineWidth = 10

// start the drawing
ctx.beginPath()
ctx.moveTo(x, y)
ctx.lineTo(x, y)
ctx.stroke()


// colour hueing
let hue = 0


// write a draw function

function draw({key}) {
    console.log(key)
    hue += 1
    console.log(hue)
    ctx.strokeStyle = `hsl(${Math.random() * 360}, 100%, 50%)`
    console.log(ctx.strokeStyle)
    ctx.beginPath()
    ctx.moveTo(x, y)
    switch (key) {
        case 'ArrowUp':
          y = y- MOVE_AMOUNT;
          break;
        case 'ArrowRight':
          x = x + MOVE_AMOUNT;
          break;
        case 'ArrowDown':
          y = y + MOVE_AMOUNT;
          break;
        case 'ArrowLeft':
          x = x - MOVE_AMOUNT;
          break;
        default:
          break;
      }
    ctx.lineTo(x, y)
    ctx.stroke()
}
// write a handler for the keys

function handleKey(e) {
    if (e.key.includes('Arrow')) {
        draw({ key: e.key})
    e.preventDefault()
    }
}

// clear / shake function

function clearCanvas() {
    canvas.classList.add('shake')
    ctx.clearRect(0, 0, width, height);
    canvas.addEventListener('animationend', () => {
        canvas.classList.remove('shake')
        // canvas.removeEventListener()
    }, { once: true}) // for replacing canvas.removeEventListener()
}

// lsiten for arrow keys

window.addEventListener('keydown', handleKey)
shakeButton.addEventListener('click', clearCanvas)