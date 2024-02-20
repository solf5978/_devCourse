#[derive(Debug, Clone, Copy)]
enum Position {
    Manager,
    Supervisor,
    Worker,
}

#[derive(Debug)]
struct Employee {
    pos: Position,
    working_hours: u32,
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
}