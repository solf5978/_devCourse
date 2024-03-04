fn main() {
    let num_vec = vec![10, 20, 30, 40];

    for num in &num_vec {
        if num == &30 {
            println!("thirty");
        } else {
            println!("{num:?}");
        }

        match num {
            30 => println!("thirty"),
            _ => println!("{num:?}"),
        }
    }
    println!("num of elements -> {:?}", num_vec.len());
}
