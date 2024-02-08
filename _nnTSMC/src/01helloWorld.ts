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

function addTGT(value: any): any {
    return value + value
}

const resultAny = addTGT("hello")
const resultAny2 = addTGT(3)

// useful when migrating from js to ts
// bcz using ANY won't cause errors initially


// tuples
let tuple: [string, number, boolean]

let hsla: [number, string, string, number]
hsla = [200, "100%", "50", 1]

let xy: [number, number]

function useCoords(): [number, number] {
    const lat = 100
    const long = 50
    return [lat, long]
}

const [lat, long] = useCoords()

// named tuples

let users: [name: string, age: number]
users = ['peach', 25]
console.log(users[0])


// interfaces

interface Author {
    name:string,
    avatar: string, 
}

const authorOne: Author = {
    name: 'mario', 
    avatar: '/img/avatarOne.png',
}

interface Post {
    title: string,
    body: string,
    tags: string[],
    create_at: Date,
    author: Author,
}

const newPost: Post = {
    title: 'my first post', 
    body: 'something', 
    tags: ['gaming', 'tech'],
    create_at: new Date(),
    author: authorOne
}