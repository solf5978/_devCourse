fn main() {
    let val1 = 5;
    let val2 = 2;
    let ans = val1 % val2;

    println!("{}", ans);

    let mut vec = vec![2, 4, 6, 8, 10];
    println!("{:?}", vec);
    vec.pop();
    vec.push(12);
    println!("{:?}", vec);

    let str1 = String::from("Hello");
    let ans = concat_string(str1);

    println!("{}", ans);
}

fn concat_string(v: String) -> String {
    v + "  World!"
}
fn control_flow(v: i32) {
    if v == 1 {
        println!("The Value -> {}", v);
    } else if v > 50 {
        println!("Value {} > 50 -> ", v);
    } else if v < 25 {
        println!("Value {} <  25-> ", v);
    } else {
        println!("The Value {} > 25 & < 50 -> ", v);
    }
}
