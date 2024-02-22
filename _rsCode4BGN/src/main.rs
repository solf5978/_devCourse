#[derive(Debug)]
enum MenuChoice {
    MainMenu,
    Start,
    Quit,
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
