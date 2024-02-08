interface Collection<T> {
    data: T[]
    name: string
}

const collectionOne: Collection<string> = {
    data: ['ehlo', 'peach', 'watermelon'],
    name: 'hello world'
}

const collectionTwo: Collection<number> = {
    data: [1, 2,3, 4,5, 6,],
    name: "a collection of number"
}

function randomCollectionItem<T>(c: Collection<T>): T {
    const i = Math.floor(Math.random() * c.data.length)
    return c.data[i]
}

const resultOne = randomCollectionItem<string>(collectionOne)
const resultTwo = randomCollectionItem(collectionTwo)