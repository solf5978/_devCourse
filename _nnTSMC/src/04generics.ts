import { log } from "console"

function logAndReturnString(val: string) : string {
    console.log(val)
    return val
}

function logAndReturnValue(val: any) : any {
    console.log(val)
    return val
}

function logReturnGenerics<T>(val: T) : T {
    console.log(val)
    return val
}

const resultOne = logReturnGenerics<string>('mario')
const resultTwo = logReturnGenerics<number>(13)

function getRandomArrayValue<T>(values: T[]): T {
    const i = Math.floor(Math.random() * values.length)
    return values[i]
}

interface User {
    name: string
    score: number
}

const users: User[] = [
    { name: 'mario', score: 100 },
    { name: 'mari', score: 900 },
    { name: 'maro', score: 70 },
    { name: 'maio', score: 200 },
]

const randomUser = getRandomArrayValue<User>(users)
console.log(randomUser)