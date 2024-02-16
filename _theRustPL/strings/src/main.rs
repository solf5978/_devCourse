
fn strings() {
    let s:&'static str = "hello there!"; // &str -> string slice
    // cannot reassign
    for c in s.chars() {
        println!("{}", c);
    }
}

fn main() {
    println!("Hello, world!");
    strings();
}
