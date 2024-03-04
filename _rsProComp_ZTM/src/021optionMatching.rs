struct Student {
    name: String,
    locker: Option<i32>,
}

fn main() {
    let mary = Student {
        name: String::from("Mary"),
        locker: Some(3),
    };

    println!("student -> {:?}", mary.name);
    match mary.locker {
        Some(num) => println!("locker num -> {num:?}"),
        None => println!("does not have a locker"),
    }
}
