struct Adult {
    age: u8,
    name: String,
}

impl Adult {
    fn new(name: &str, age: u8) -> Result<Self, &str> {
        if age >= 21 {
            Ok(Self {
                age,
                name: name.to_string(),
            })
        } else {
            Err("Age must be at least 21")
        }
    }
}

fn main() {
    let adult_one = Adult::new("13", 17);
    let adult_two = Adult::new("Sajd", 21);
    match adult_one {
        Ok(child) => println!("{} is {} years old", child.name, child.age),
        Err(e) => println!("{e}"),
    }
    match adult_two {
        Ok(child) => println!("{} is {} years old", child.name, child.age),
        Err(e) => println!("{e}"),
    }
}
