use std::collections::HashMap;
use std::io;
struct Bill {
    name: String,
    amount: f64,
}

struct Bills {
    inner: HashMap<String, Bill>,
}

impl Bills {
    fn new() -> Self {
        Self { inner: vec![] }
    }

    fn add(&mut self, bill: Bill) {
        self.inner.insert(bill.name.clone(), bill);
    }

    fn get_all(&self) -> Vec<Bill> {
        let mut bills = vec![];
        for bill in self.inner.values() {
            bills.push(bill.clone());
        }
        bills
    }

    fn remove(&mut self, name: &str) -> bool {
        self.inner.remove(name).is_some()
    }
}

fn get_input() -> String {
    let mut buf = String::new();
    while io::stdin().read_line(&mut buf).is_err() {
        println!("Please Re-Enter Your Data");
    }
    buf.trim().to_owned()
}

fn get_bill_amount() -> f64 {
    println!("Amount: ");
    loop {
        let input: String = get_input();
        let parsed_input: Result<f64, _> = input.parse();
        match parsed_input {
            Ok(amount) => return amount,
            Err(_) => println!("Please Re-Enter A Number: "),
        }
    }
}

fn add_bill_menu(bills: &mut Bills) {
    println!("Bill Name: ");
    let name = get_input();
    let amount = get_bill_amount();
    let bill = Bill { name, amount };
    bills.add(bill);
    println!("Bill Added");
}

fn remove_bill_menu(bills: &mut Bills) {
    for bill in bills.get_all() {
        println!("{:?}", bill);
    }
    let input = get_input();
}

fn view_bills_menu(bills: &Bills) {
    for bill in bills.get_all() {
        println!("{:?}", bill);
    }
}

fn main_menu() {
    fn show() {
        println!("");
        println!("-- Manage Bills --");
        println!("1. Add New Bill");
        println!("2. View Bills");
        println!("");
        println!("Selection:");
    }

    let mut bills = Bills::new();

    loop {
        show();
        let input = get_input();
        match input.as_str() {
            "1" => add_bill_menu(&mut bills),
            "2" => view_bills_menu(&bills),
            _ => break,
        }
    }
}

fn main() {
    main_menu();
}
