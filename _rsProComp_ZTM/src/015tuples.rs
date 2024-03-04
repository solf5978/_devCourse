fn display_result(result: bool) {
    match result {
        true => println!("greater than 100"),
        false => println("less than 100"),
    }
}
fn main() {
    let value = 100;
    let is_gt_100 = value > 100;
    let is_lt_100 = value < 100;
    display_result(is_gt_100);
    display_result(is_lt_100);
}
