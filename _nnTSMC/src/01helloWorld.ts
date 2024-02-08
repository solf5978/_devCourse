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

// interface as argument types

function createPost(post: Post): void {
    console.log(`Created post ${post.title} by ${post.author.name}`)
}

createPost(newPost)

// interface with arrays
let posts: Post[] = []

posts.push(newPost)

// TYPE aliases as tuple

type Rgb = [number, number, number]

function getRandomColor() :Rgb {
    const r = Math.floor(Math.random() * 255)
    const g = Math.floor(Math.random() * 255)
    const b = Math.floor(Math.random() * 255)
    return [r, g, b,]
}

const colorOne = getRandomColor()
const colorTwo = getRandomColor()
console.log(colorOne, colorTwo)
// TYPE aliases as object literal

type User = {
    name: string
    score: number 
}

const userOne: User = {
    name: 'marios',
    score: 55
}

function formatUser(user: User) : void {
    console.log(`${user.name} got ${user.score}`)
}

formatUser(userOne)
formatUser({ name: 'yoshi', score: 31})

// union types

let someId: number | string
someId = 1
someId = '2'

let email: string | null = null

email = 'marios@netninja.dev'
email = null

type Id = number | string
let anotherId: Id

anotherId = '1hjk2ld;s'
anotherId = 5

// union type pitfall

function swapIdType(id: Id) : Id {
    // only use in props and methods common to both number and string types
    // parseInt(id) is a NoNo
    return id
}

// type guards
function swapIdType_guard(id: Id) {
    if (typeof id === 'string') {
        // use on strings
        return parseInt(id)
    } else {
        // that is a number as it shall be
        return `${id}`
    }
}

const idOne = swapIdType_guard(1)
const idTwo = swapIdType_guard("2")
console.log(idOne)
console.log(idTwo)

// tagged interfaces

interface PerUser {
    type: 'user'
    username: string
    email: string
    id: Id
}

interface PerPerson {
    type: 'person'
    firstName: string
    age: number
    id: Id
}

function logDetails(value: PerUser | PerPerson) : void {
    // use of hardcoded type to verify
    if (value.type === 'user'){
        value.email == "hello@"
    }
    if (value.type === 'person') {
        value.firstName = "hello"
    }
}

// reusable interfaces

interface hasQuantity {
    quantity: number
}

const some1thing: hasQuantity = {quantity:50}
function printQuantity(item: hasQuantity) : void {
    console.log(`the qty of the item is ${item.quantity}`)
}

const fruit = {
    name: 'mango',
    quantity: 50,
}

const vehicle = {
    type: 'car',
    quantity: 3,
}

const sigPerson = {
    name: 'mario',
    age: 30,
}

// function signatures

type Calculator = (numOne: number, numTwo: number) => number

function exampleOne(a: number, b: number) {
    return a + b
}

function exampleTwo(first: number, second: number) {
    return first * second
}

function exampleThree(num: number) {
    return num * num
}

function exampleFour(numOne: number, numTwo: number) {
    return `${numOne}${numTwo}`
}

let calcs: Calculator[] = []
calcs.push(exampleOne)
calcs.push(exampleTwo)
calcs.push(exampleThree)
// function signatures on interface

interface HasArea {
    name: string
    calcArea: (a: number) => number
    sameThing(a:number) : number
}

const shapeOne: HasArea = {
    name: "square",
    calcArea(l: number) {
        return l* l
    },
    sameThing(l) {
        return l
    }
}

const shapeTwo: HasArea = {
    name: "circle",
    calcArea(r: number) {
        return Math.PI * r^2
    },
    sameThing(l) {
        return l
    }
}


shapeOne.calcArea(5)
shapeTwo.calcArea(10)

// extending interfaces

interface HasFormatter {
    format() : string
}

interface Bill extends HasFormatter {
    id : string | number
    amount: number
    server: string
}

const usr = {
    id: 1, 
    format(): string {
        return `This user has an id of ${this.id}`
    }
}

const bill = {
    id: 2, 
    amount: 50,
    server: 'marios',
    format(): string {
        return `Bill with id ${this.id} has ${this.amount} to pay`
    }
}

function printBillFormat(value: HasFormatter) : void {
    console.log(value.format())
}