fn main() {
    let val = 5;
    let val2 = Box::new(2);
    println!("{}", val * *val2);
}
