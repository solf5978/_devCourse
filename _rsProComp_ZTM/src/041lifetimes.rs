fn longest<'a>(first: &'a str, second: &'a str) -> &'a str {
    if second > first {
        second
    } else {
        first
    }
}
fn main() {
    let short = "hello";
    let long = "this is a long message";
    println!("{}", longest(short, long));
}
