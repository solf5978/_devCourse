
interface HasId {
    id: number
}

class DataCollection<T extends HasId> {
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

    deleteOne(id: number) : void {
        this.data = this.data.filter((item) => item.id !== id)
    }
}

interface demoU {
    name: string
    score: number
    id: number
}

const gen_user = new DataCollection<demoU>([
    { name: 'shaun', score: 125, id: 1 },
    { name: 'shaun', score: 125, id: 2 },
    { name: 'shaun', score: 125, id: 3 },
])

gen_user.add( { name: 'shuan', score: 100, id: 3})
gen_user.deleteOne(2)

console.log('load one - ', gen_user.loadOne)
console.log('load all - ', gen_user.loadAll)