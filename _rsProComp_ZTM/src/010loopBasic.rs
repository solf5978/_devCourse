fn main() {
    let mut num = 1;
    loop {
        if num < 5 {
            println!("{num:?}");
        } else {
            break;
        }
        num = num + 1;
    }
}
