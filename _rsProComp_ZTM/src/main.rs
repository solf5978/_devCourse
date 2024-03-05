use std::io;

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
fn main() {}
