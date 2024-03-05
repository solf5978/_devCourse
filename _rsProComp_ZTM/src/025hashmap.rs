use std::{collections::HashMap, fmt::format};

fn main() {
    let mut stock = HashMap::new();
    stock.insert("chair", 5);
    stock.insert("lamp", 5);
    stock.insert("bed", 5);
    stock.insert("couch", 5);
    stock.insert("table", 5);
    let mut total_stock = 0;

    for (item, qty) in stock.iter() {
        total_stock = total_stock + qty;
        let stock_count = if qty == &0 {
            "out of stock".to_owned()
        } else {
            format!("{qty:?}")
        };
        println!("item -> {item:?} and its stock is {qty:?}");
    }
    println!("{total_stock:?}");
}
