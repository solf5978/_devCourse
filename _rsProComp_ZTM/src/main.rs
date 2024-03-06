use std::{collections::HashMap, io};
#[derive(Clone, Debug)]
pub struct Bill {
    name: String,
    amount: f64,
}

pub struct Bills {
    inner: HashMap<String, Bill>,
}

impl Bills {
    fn new() -> Self {
        Self {
            inner: HashMap::new(),
        }
    }

    fn add(&mut self, bill: Bill) {
        self.inner.insert(bill.name.to_string(), bill);
    }

    fn get_all(&self) -> Vec<&Bill> {
        self.inner.values().collect()
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

mod menu {
    use crate::{get_bill_amount, get_input, Bill, Bills};

    pub fn add_bill(bills: &mut Bills) {
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
        println!("Bill Added")
    }

    pub fn remove_bill(bills: &mut Bills) {
        for bill in bills.get_all() {
            println!("{bill:?}");
        }
        println!("Enter bill name to remove: ");
        let name = match get_input() {
            Some(name) => name,
            None => return,
        };
        if bills.remove(&name) {
            println!("Bill Removed");
        } else {
            println!("Bill Not Found");
        }
    }

    pub fn update_bill(bills: &mut Bills) {
        for bill in bills.get_all() {
            println!("{bill:?}")
        }
        println!("Enter bill name to update: ");
        let name = match get_input() {
            Some(name) => name,
            None => return,
        };
        let amount = match get_bill_amount() {
            Some(amount) => amount,
            None => return,
        };
        if bills.update(&name, amount) {
            println!("Bill updated");
        } else {
            println!("Bill Not Found");
        }
    }

    pub fn view_bills(bills: &Bills) {
        for bill in bills.get_all() {
            println!("{bill:?}")
        }
    }
}
enum MainMenu {
    AddBill,
    ViewBill,
    RemoveBill,UpdateBill,RevertOperation,
}

impl MainMenu {
    fn from_str(input: &str) -> Option<MainMenu> {
        match input {
            "1" => Some(Self::AddBill),
            "2" => Some(Self::ViewBill),
            "3" => Some(Self::RemoveBill),
            "4" => Some(Self::UpdateBill),
            "5" => Some(Self::RevertOperation),
            _ => None,
        }
    }

    fn show() {
        println!();
        println!("-- Manage Bills --");
        println!("1. Add New Bill");
        println!("2. View Bills");
        println!("3. Delete Bills");
        println!("4. Update Bills");
        println!("5. Revert Operation");
        println!();
        println!("Selection:");
    }
}

fn get_input() -> Option<String> {
    let mut buf = String::new();
    while io::stdin().read_line(&mut buf).is_err() {
        println!("Please re-enter your data");
    }

    let input = buf.trim().to_owned();
    if input.is_empty() {
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
        if input.is_empty() {
            return None;
        }
        let parsed_input: Result<f64, _> = input.parse();
        match parsed_input {
            Ok(amount) => return Some(amount),
            Err(_) => println!("Please Re-Enter A Number: "),
        }
    }
}

fn main() {
    let mut bills = Bills::new();
    loop {
        MainMenu::show();
        let input = get_input().expect("No Input");
        match MainMenu::from_str(input.as_str()) {
            Some(MainMenu::AddBill) => menu::add_bill(&mut bills),
            Some(MainMenu::ViewBill) => menu::view_bills(&bills),
            Some(MainMenu::RemoveBill) => menu::remove_bill(&mut bills),
            Some(MainMenu::UpdateBill)
            None => return,
        }
    }
}
