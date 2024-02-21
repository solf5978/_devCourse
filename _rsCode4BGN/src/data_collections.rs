
struct Person {
    name: String,
    fav_color: String,
    age: u8,
}

impl Person {
    fn props(&self) {
        println!("{}", (self.name));
        println!("{}", (self.fav_color));
        println!("{}", (self.age));
    }
}

fn main() {
    let my_num = vec![10, 20, 30, 40];

    for num in &my_num {
        match num {
            30 => println!("30"),
            _ => println!("{:?}", num),
        }
    }
    println!("number of elements = {:?}", my_num.len());

    let people = vec![
        Person {
            name: String::from("george"),
            fav_color: String::from("Green"),
            age: 8,
        },
        Person {
            name: String::from("Anna"),
            fav_color: String::from("Purple"),
            age: 9,
        },
        Person {
            name: String::from("Katie"),
            fav_color: String::from("Blue"),
            age: 14,
        },
    ];

    for person in &people {
        if person.age <= 10 {
            person.props();
        }
    }
}
