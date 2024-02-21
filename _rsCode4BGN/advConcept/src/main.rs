#[derive(Debug, Clone, Copy)]
enum Position {
    Manager,
    Supervisor,
    Worker,
}

#[derive(Debug, Clone, Copy)]
struct Employee {
    pos: Position,
    working_hours: u32,
}

fn pEmployee(emp : Employee) {
    println!("{:?}", emp);
}

enum Discount {
    Percent(i32),
    Flat(i32),
}

struct Ticket {
    event: String,
    price: i32,
}

fn main() {
    let me = Employee {
        pos: Position::Worker,
        working_hours: 40,
    };

    // match me.pos {
    //     Position::Manager => println!("A Manager"),
    //     Position::Supervisor => println!("A Supervisor"),
    //     Position::Worker => println!("A Worker"),
    // }

    //Using #[derive(Debug)] on Enum
    println!("{:?}", me.pos);

    //Using #[derive(Debug)] on Struct
    println!("{:?}", me);
    pEmployee(me);
    pEmployee(me);

    let n = 3;
    match n {
        3 => println!("three"),
        other => println!("number: {:?}", other),
    }

    let flat = Discount::Flat(2);
    match flat {
        Discount::Flat(2) => println!("flat 2"),
        Discount::Flat(amount) => println!("flat discount of {:?}", amount),
        _ => (),
    }

}