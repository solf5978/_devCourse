fn add_two_nums(a: i32, b: i32) -> i32 {
    a + b
}

fn display_result(result: i32) {
    println!("{result:?}");
}

fn main() {
    display_result(add_two_nums(5, 8))
}
