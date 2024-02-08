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