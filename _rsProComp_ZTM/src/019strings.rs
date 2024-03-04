struct Person {
    age: i32,
    name: String,
    fav_color: String,
}

impl Person {
    fn new(age: i32, name: String, fav_color: String) -> Self {
        Self {
            age,
            name,
            fav_color,
        }
    }
}

fn print(data: &str) {
    println!("{data:?}");
}

fn main() {
    let people = vec![
        Person::new(8, "george".to_owned(), String::from("green")),
        Person::new(15, String::from("hallo"), "favorite color".to_owned()),
        Person::new(29, "aladskalfjda".to_owned(), String::from("yello")),
    ];

    for person in people {
        if person.age >= 10 {
            print(&person.name);
            print(&person.fav_color);
            println!("{:?}", person.age);
        }
    }
}
