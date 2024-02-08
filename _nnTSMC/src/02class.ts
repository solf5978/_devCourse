type Base = 'classic' | 'thick' | 'thin' | 'garlic'

class Pizzas {
    constructor(title: string, price: number) {
        this.title = title
        this.price = price
    }
    title: string
    price: number
    base: Base = 'classic'
    toppings: string[] = []

    addTopping(topping: string) : void {
        this.toppings.push(topping)
    }

    removeTopping(topping: string) : void {
        this.toppings = this.toppings.filter((t) => !== topping)
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
