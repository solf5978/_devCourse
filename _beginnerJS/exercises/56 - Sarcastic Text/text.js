const textArea = document.querySelector('[name="text"]')
const result = document.querySelector('.result')
const filterInputs = Array.from(document.querySelectorAll('[name="filter"]'))

const funkyLetters = {
    '-': '₋', '!': 'ᵎ', '?': 'ˀ', '(': '⁽', ')': '₎', '+': '⁺', '=': '₌', '0': '⁰', '1': '₁', '2': '²', '4': '₄', '5': '₅', '6': '₆', '7': '⁷', '8': '⁸', '9': '⁹', a: 'ᵃ', A: 'ᴬ', B: 'ᴮ', b: 'ᵦ', C: '𝒸', d: 'ᵈ', D: 'ᴰ', e: 'ₑ', E: 'ᴱ', f: '𝒻', F: 'ᶠ', g: 'ᵍ', G: 'ᴳ', h: 'ʰ', H: 'ₕ', I: 'ᵢ', i: 'ᵢ', j: 'ʲ', J: 'ᴶ', K: 'ₖ', k: 'ₖ', l: 'ˡ', L: 'ᴸ', m: 'ᵐ', M: 'ₘ', n: 'ₙ', N: 'ᴺ', o: 'ᵒ', O: 'ᴼ', p: 'ᵖ', P: 'ᴾ', Q: 'ᵠ', q: 'ᑫ', r: 'ʳ', R: 'ᵣ', S: 'ˢ', s: 'ˢ', t: 'ᵗ', T: 'ₜ', u: 'ᵘ', U: 'ᵤ', v: 'ᵛ', V: 'ᵥ', w: '𝓌', W: 'ʷ', x: 'ˣ', X: 'ˣ', y: 'y', Y: 'Y', z: '𝓏', Z: 'ᶻ'
  };

function transformText(text) {
    //const filterChecked = document.querySelector('[name="filter"]:checked').value
    const filterChecked = filterInputs.find(input => input.checked).value
    const mod = Array.from(text).map(filters[filterChecked])
    result.textContent = mod.join('')
}

const filters = {
    sarcastic(letter, index) {
        if ( index % 2){
            return letter.toUpperCase()
        }
        return letter.toLowerCase()
    },
    funky(letter, ) {
        if (funkyLetters[letter] || funkyLetters[letter.toLowerCase()]) {
            return funkyLetters[letter]
        }
        return letter
    },
    unable(letter, ) {
        const randIndex = Math.floor(Math.random() * 3)
        if (letter === '' && random === 2) {
            return '...'
        }
        return letter
    }
}

textArea.addEventListener('input', e => transformText(e.target.value))
filterInputs.forEach(input => 
    input.addEventListener('input', () => 
    {transformText(textarea.value)}))