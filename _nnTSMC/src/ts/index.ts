import { Pizza } from "./models/Pizzas";

document.addEventListener('DOMContentLoaded', async() => {
    // load the pizza data
    const pizzas = await Pizza.loadAll()
})