fn main() {
    let mut num = 1;
    loop {
        if num < 5 {
            println!("{num:?}");
            num = num + 1;
        } else {
            break;
        }
    }
}
