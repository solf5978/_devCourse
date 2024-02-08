type Base = 'classic' | 'thick' | 'thin' | 'garlic'

interface HasFormatter {
    format() : string
}

class MenuItem implements HasFormatter {
    constructor(private title: string, private price:number){}
    // use get as a getter keyword
    get details() : string {
        return `${this.title} - ${this.price}`
    }

    format() {
        return `This menu item is call ${this.title} and is ${this.price}`
    }
}

class Pizzas extends MenuItem{
    constructor(title: string, price: number) {
        super(title, price)
    }
    // private title: string
    // private price: number
    private base: Base = 'classic'
    private toppings: string[] = []

    addTopping(topping: string) : void {
        this.toppings.push(topping)
    }

    removeTopping(topping: string) : void {
        this.toppings = this.toppings.filter((t) => t !== topping)
    }

    selectBase(b: Base): void {
        this.base = b
    }
}

const pizza = new Pizzas('marios special', 15)
const pizzaTwo = new Pizzas('luigi special', 30)

pizza.addTopping('mushrooms')
pizza.addTopping('olives')
pizza.selectBase('garlic')

function addMushroomsToPizzas(pizzas: Pizzas[]): void {
    for (const p of pizzas) {
        p.addTopping('mushrooms')
    }
}

addMushroomsToPizzas([pizza, pizzaTwo])
// pizza.details() <- call a function
// use as a getter
pizza.details

function printMenuItem(item: MenuItem) : void {
    console.log(item.details)
}

printMenuItem(pizza)

function printFormatted(val: HasFormatter) : void {
    console.log(val.format())
}