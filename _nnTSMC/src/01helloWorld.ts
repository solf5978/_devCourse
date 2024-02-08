let age: number = 30
let start: string = "Hello World"
let isFictional:boolean

isFictional = true
console.log(age)
console.log(start)
console.log(isFictional)

// null & undefined

let something: null
let anotherThing: undefined

// Arrays
let names: []
let str_names: string[]
let ppl: string[] = ['marios', 'luigi']
let ages: number[] = [25, 26, 20]

const f = ppl[1]

ppl.push("hello")
ages.push(35)


let things = [1, true, 'hello']
// const t -> number boolean string, either one of these
const t = things[0]

// object literals

let user: {
    firstName:string,
    age: number, 
    id: number,
} = {   firstName: 'mario',
        age: 18,
        id: 1, }

user.firstName = "djafh"

// type inference with object literals

let person = {
    name: 'luigi',
    score: 35
}

function addTwoNumbers(a: number, b: number): number {
    return a + b
}

const subtractTwoNumbers = (a: number, b:number): number => {
    return a - b 
}

function addAllNumbers(items:number[]): void {
    const total = items.reduce((a, c ) => a + c, 0)
    console.log(total)
}

function formatGreeting(name: string, greeting: string): string {
    return `${greeting}, ${name}`
}

let age1: any
let anytype

let anythings: any[] = ['hello', 30, null, true]
anythings.push({id: 123})