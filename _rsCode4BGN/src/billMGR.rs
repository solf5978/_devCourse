use std::collections::HashMap;
use std::io;

#[derive(Debug, Clone)]
struct Bill {
    name: String,
    amount: f64,
}

struct Bills {
    inner: HashMap<String, Bill>,
}

impl Bills {
    fn new() -> Self {
        Self {
            inner: HashMap::new(),
        }
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

    fn update(&mut self, name: &str, amount: f64) -> bool {
        match self.inner.get_mut(name) {
            Some(bill) => {
                bill.amount = amount;
                true
            }
            None => false,
        }
    }
}

fn get_input() -> Option<String> {
    let mut buf = String::new();
    while io::stdin().read_line(&mut buf).is_err() {
        println!("Please Re-Enter Your Data");
    }
    let input = buf.trim().to_owned();
    if input == "" {
        None
    } else {
        Some(input)
    }
}

fn get_bill_amount() -> Option<f64> {
    println!("Amount: ");
    loop {
        let input = match get_input() {
            Some(input) => input,
            None => return None,
        };
        if &input == "" {
            return None;
        }
        let parsed_input: Result<f64, _> = input.parse();
        match parsed_input {
            Ok(amount) => return Some(amount),
            Err(_) => println!("Please Re-Enter A Number: "),
        }
    }
}

fn add_bill_menu(bills: &mut Bills) {
    println!("Bill Name: ");
    let name = match get_input() {
        Some(input) => input,
        None => return,
    };
    let amount = match get_bill_amount() {
        Some(amount) => amount,
        None => return,
    };
    let bill = Bill { name, amount };
    bills.add(bill);
    println!("Bill Added");
}

fn remove_bill_menu(bills: &mut Bills) {
    println!("Enter bill name to update");
    for bill in bills.get_all() {
        println!("{:?}", bill);
    }
    let input = match get_input() {
        Some(input) => input,
        None => return,
    };
    if bills.remove(&input) {
        println!("Removed");
    } else {
        println!("Bill not found");
    }
}

fn update_bill_menu(bills: &mut Bills) {
    for bill in bills.get_all() {
        println!("{:?}", bill);
    }
    println!("Enter bill name to update");
    let input = match get_input() {
        Some(input) => input,
        None => return,
    };
    let amount = match get_bill_amount() {
        Some(amount) => amount,
        None => return,
    };
    if bills.update(&input, amount) {
        println!("updated");
    } else {
        println!("bill not found");
    }
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
        println!("3. Delete Bills");
        println!("4. Update Bills");
        println!("5. Revert Operation");
        println!("");
        println!("Selection:");
    }

    let mut bills = Bills::new();

    loop {
        show();
        let input = match get_input() {
            Some(input) => input,
            None => return,
        };
        match input.as_str() {
            "1" => add_bill_menu(&mut bills),
            "2" => view_bills_menu(&bills),
            "3" => remove_bill_menu(&mut bills),
            "4" => update_bill_menu(&mut bills),
            _ => break,
        }
    }
}

fn main() {
    main_menu();
}
