
interface HasID {
    id: number
}

function addIdToValue<T>(val: T): T & HasID{
    const id = Math.random()

    return { ...val, id }
}

interface PostInte {
    title: string
    thumbsUp: number
}

const post = addIdToValue<PostInte>({ title: "Hello", thumbsUp:250 })
console.log(post.thumbsUp)