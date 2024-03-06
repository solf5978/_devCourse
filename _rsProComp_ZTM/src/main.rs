use std::io;
#[derive(Clone, Debug)]
pub struct Bill {
    name: String,
    amount: f64,
}

pub struct Bills {
    inner: Vec<Bill>,
}

impl Bills {
    fn new() -> Self {
        Self { inner: vec![] }
    }

    fn add(&mut self, bill: Bill) {
        self.inner.push(bill);
    }

    fn get_all(&self) -> Vec<&Bill> {
        self.inner.iter().collect()
    }

    fn view() {}
}

mod menu {
    use crate::{get_input, Bill, Bills};

    pub fn add_bill(bills: &mut Bills) {
        println!("Bill Name: ");
        let name = match get_input() {
            Some(input) => input,
            None => return,
        };
        let amount = match get_input() {
            Some(amount) => amount,
            None => return,
        };
        let bill = Bill { name, amount };
        bills.add(bill);
        println!("Bill Added")
    }
}
enum MainMenu {
    AddBill,
    ViewBill,
}

impl MainMenu {
    fn from_str(input: &str) -> Option<MainMenu> {
        match input {
            "1" => Some(Self::AddBill),
            "2" => Some(Self::ViewBill),
            _ => None,
        }
    }

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
}

fn get_input() -> Option<String> {
    let mut buf = String::new();
    while io::stdin().read_line(&mut buf).is_err() {
        println!("Please re-enter your data");
    }

    let input = buf.trim().to_owned();
    if input == "" {
        None
    } else {
        Some(input)
    }
}
fn main() {
    loop {
        MainMenu::show();
        let input = get_input().expect("No Input");
        match MainMenu::from_str(input.as_str()) {
            Some(MainMenu::AddBill) => (),
            Some(MainMenu::ViewBill) => (),
            None => return,
        }
    }
}
