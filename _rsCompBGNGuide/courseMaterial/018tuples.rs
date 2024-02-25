#[allow(unused_variables)]
#[allow(unused_assignments)]

fn main() {
    let mut person: (&str, i64, bool) = ("John", 27, true);
    println!("{:?}", person);
    println!("{:?}", person.0);
    person.0 = "Mike";
    println!("{:?}", person.0);
    let (name, age, employment) = person;
    println!("name: {}, age: {}, employed: {}", name, age, employment);
}