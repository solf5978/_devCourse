fn main() {
    let num_vec = vec![10, 20, 30, 40];

    for num in num_vec {
        if num == 30 {
            println!("thirty");
        } else {
            println!("{num:?}");
        }
    }
}
