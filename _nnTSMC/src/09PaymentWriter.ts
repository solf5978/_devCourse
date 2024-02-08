import { CSVWriter } from "./08CSVWriter"

interface Payment {
    id: number
    amount: number
    to: string
    notes: string
}

const paymentwriter = new CSVWriter<Payment>(['id', 'amount', 'to', 'notes'])

paymentwriter.addRows([
    { id: 1, amount: 50, to: 'yoshi', notes: 'for--'},
    { id: 13, amount: 510, to: 'ygdsaoshi', notes: 'fordas--'},
])

paymentwriter.save('./data/payments.csv')