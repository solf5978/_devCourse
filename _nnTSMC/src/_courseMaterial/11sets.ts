const set_name = new Set<string>()

set_name.add('marios')
set_name.add('mario3s')
set_name.add('mario2s')
set_name.add('mario4s')

console.log(set_name)

interface setUser {
    email: string
    score: number
}

const user1: setUser = { email: 'hello@123.dev', score: 10 }
const user2: setUser = { email: 'world@456.dev', score: 15 }

const users_1 = new Set<setUser> ()

users_1.add(user1)
users_1.add(user1)
users_1.add(user2)

function logUserEmails(users: Set<setUser>) : void {
    users.forEach((user) => console.log(user.email))
}

