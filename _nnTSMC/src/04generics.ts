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