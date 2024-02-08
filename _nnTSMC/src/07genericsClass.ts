
class DataCollection<T> {
    constructor(private data: T[]){}

    loadOne(): T{
        const i = Math.floor(Math.random() * this.data.length)
        return this.data[i]
    }
    
    loadAll(): T[] {
        return this.data
    }

    add(val: T) : T[] {
        this.data.push(val)
        return this.data
    }
}

interface demoU {
    name: string
    score: number
}

const gen_user = new DataCollection<demoU>([
    { name: 'shaun', score: 125 },
    { name: 'shaun', score: 125 },
    { name: 'shaun', score: 125 },
])

gen_user.add( { name: 'shuan', score: 100})

console.log('load one - ', gen_user.loadOne)
console.log('load all - ', gen_user.loadAll)