fn main() {
    let mut num = 0;
    loop {
        if num < 5 {
            println!("{num:?}");
            num = num + 1;
        } else {
            break;
        }
    }
}
