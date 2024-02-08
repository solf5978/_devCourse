import { CSVWriter } from "./08CSVWriter"

interface Payment {
    id: number
    amount: number
    to: string
    notes: string
}

const writer = new CSVWriter(['id', 'amount', 'to', 'notes'])

writer.addRows([
    { id: 1, amount: 50, to: 'yoshi', notes: 'for--'},
    { id: 13, amount: 510, to: 'ygdsaoshi', notes: 'fordas--'},
])

writer.save('./data/payments.csv')