use activity::math::{add, minus};
use activity::msg::{capitalize, trim};
use chrono::prelude::*;
fn main() {
    let utc: DateTime<Utc> = Utc::now();
    let local: DateTime<Local> = Local::now();
    println!("{local:?}");
}
