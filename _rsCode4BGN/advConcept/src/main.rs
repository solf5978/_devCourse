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

fn pEmployee(emp: Employee) {
    println!("{:?}", emp);
}

enum Discount {
    Percent(i32),
    Flat(i32),
}

struct EventTicket {
    event: String,
    price: i32,
}

enum Ticket {
    Backstage(f64, String),
    Standard(f64),
    Vip(f64, String),
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

    let concert = EventTicket {
        event: "concert".to_owned(),
        price: 50,
    };

    match concert {
        EventTicket { price: 50, event } => println!("price @ 50 -> {:?}", event),
        EventTicket { price, .. } => println!("price = {:?}", price),
    }

    let tickets = vec![
        Ticket::Backstage(50.0, "Billy".to_owned()),
        Ticket::Standard(15.0),
        Ticket::Vip(30.0, "Amy".to_owned()),
    ];

    for ticket in tickets {
        match ticket {
            Ticket::Backstage(price, holder) => {
                println!("Backstage ticker holder: {:?}, price: {:?}", holder, price)
            }
            Ticket::Standard(price) => println!("Standard ticker price: {:?}", price),
            Ticket::Vip(price, holder) => {
                println!("Vip ticker holder: {:?}, price: {:?}", holder, price)
            }
        }
    }
}
