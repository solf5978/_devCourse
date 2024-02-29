fn check_val(val: &Vec<i8>) -> bool {
    if val[0] == 1 {
        return true;
    } else {
        return false;
    }
}

fn add_two(v: i8) {
    v + 2;
}
fn main() {
    let mut vec = vec![1, 3, 5, 7];
    println!("{:?}", check_val(&vec));
    vec.push(15);
    println!("{:?}", vec);

    let mut value = 2;
    add_two(value);
    println!("{}", value);
    value = 5;
    println!("{}", value);
}
