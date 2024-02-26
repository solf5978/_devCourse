use crate::Colors::Red;
use crate::Person::Name;

#[allow(unused_variables)]
#[allow(unused_assignments)]
#[allow(dead_code)]

fn main() {
    let my_color = Colors::Red;
    println!("{:?}", my_color);
    let my_color = Red;
    println!("{:?}", my_color);

    let person = Name(String::from("Alex"));
    println!("{:?}", person);
}

#[derive(Debug)]
enum Colors {
    Red,
    Green,
    Blue
}

#[derive(Debug)]
enum Person {
    Name(String),
    Surname(String),
    Age(u32)
}