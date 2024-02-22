use std::{collections::HashMap, hash::Hash};
#[derive(Debug)]
struct Contents {
    content: String,
}

#[derive(Debug)]
enum MenuChoice {
    MainMenu,
    Start,
    Quit,
}

enum Position {
    Maintenance,
    Marketing,
    Manager,
    LineSupervisor,
    KitchenStaff,
    AssemblyTech,
}

enum Status {
    Active,
    Terminated,
}

struct Employee {
    position: Position,
    status: Status,
}

fn t_access(emp: &Employee) -> Result<(), String> {
    match emp.status {
        Status::Terminated => return Err("Access Denied".to_owned()),
        _ => (),
    }

    match emp.position {
        Position::Maintenance => Ok(()),
        Position::Marketing => Ok(()),
        Position::Manager => Ok(()),
        _ => Err("Invalid position".to_owned()),
    }
}

fn p_access(emp: &Employee) -> Result<(), String> {
    let attemp_access = t_access(emp)?;
    println!("Authorized");
    Ok(())
}

fn get_choice(input: &str) -> Result<MenuChoice, String> {
    match input {
        "mainmenu" => Ok(MenuChoice::MainMenu),
        "start" => Ok(MenuChoice::Start),
        "quit" => Ok(MenuChoice::Quit),
        _ => Err("Nothing".to_owned()),
    }
}

struct Survey {
    q1: Option<i32>,
    q2: Option<bool>,
    q3: Option<String>,
}

struct Customer {
    age: i32,
}

struct Student {
    name: String,
    locker: Option<i32>,
}

fn print_choice(choice: &MenuChoice) {
    println!("choice = {:?}", choice);
}

fn try_purchase(customer: &Customer) -> Result<(), String> {
    if customer.age < 21 {
        Err("Below The Lawful Age".to_owned())
    } else {
        Ok(())
    }
}

fn pick_choice(input: &str) -> Result<(), String> {
    let choice: MenuChoice = get_choice(input)?;
    print_choice(&choice);
    Ok(())
}

fn main() {
    let mut stock = HashMap::new();
    stock.insert("chair", 5);
    stock.insert("bed", 3);
    stock.insert("teapot", 2);
    stock.insert("table", 0);
    stock.insert("lamp", 1);
    let mut total_stock = 0;
    for (item, qty) in stock.iter() {
        total_stock = total_stock + qty;
        let stock_count = if qty == &0 {
            "out of stock".to_owned()
        } else {
            format!("{:?}", qty)
        };
        println!("item -> {:?}, stock-> {:?}", item, stock_count);
    }
    println!("total stock-> {:?}", total_stock);

    let mut lockers = HashMap::new();
    lockers.insert(
        1,
        Contents {
            content: "stuff".to_owned(),
        },
    );
    lockers.insert(
        2,
        Contents {
            content: "shirt".to_owned(),
        },
    );
    lockers.insert(
        3,
        Contents {
            content: "gym shorts".to_owned(),
        },
    );

    for (locker_num, locker_val) in lockers.iter() {
        println!("number->{:?}, content->{:?}", locker_num, locker_val);
    }

    let mgr = Employee {
        status: Status::Active,
        position: Position::Manager,
    };

    match p_access(&mgr) {
        Err(e) => println!("Access Denied: {:?}", e),
        _ => (),
    }
    let ashley = Customer { age: 20 };
    let purchased = try_purchase(&ashley);
    println!("{:?}", purchased);
    let choice: Result<MenuChoice, _> = get_choice("mainmenu");
    // println!("choice = {:?}", choice);
    // match choice {
    //     Ok(inner_choice) => print_choice(&inner_choice),
    //     Err(e) => println!("error = {:?}", e),
    // };
    let res = pick_choice("start");
    println!("Choice value = {:?}", res);

    let mary = Student {
        name: "Mary".to_owned(),
        locker: Some(3),
    };

    println!("student: {:?}", mary.name);
    match mary.locker {
        Some(num) => println!("locker number -> {:?}", num),
        None => println!("no locker assigned"),
    }

    println!("Hello, world!");
    let rep = Survey {
        q1: Some(12),
        q2: Some(true),
        q3: Some("A".to_owned()),
    };

    match rep.q1 {
        Some(ans) => println!("q1: {:?}", ans),
        None => println!("q1: No rep"),
    }

    match rep.q2 {
        Some(ans) => println!("q1: {:?}", ans),
        None => println!("q2: No rep"),
    }

    match rep.q3 {
        Some(ans) => println!("q1: {:?}", ans),
        None => println!("q3: No rep"),
    }
}
