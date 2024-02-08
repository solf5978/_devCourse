type Base = 'classic' | 'thick' | 'thin' | 'garlic'

class Pizzas {
    constructor(private title: string, private price: number) {
        // this.title = title
        // this.price = price
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
