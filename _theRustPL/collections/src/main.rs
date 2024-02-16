
fn vectors() {
    let mut a = Vec::new();
    a.push(1);
    a.push(2);
    a.push(3);

    println!("a = {:?}", a);

    a.push(44);
    println!("a = {:?}", a);
    println!("a[0] = {}", a[0]);

    let idx: usize = 0;
    a[idx] = 312;
    println!("a[0] = {}", a[idx]);

    match a.get(6) {
        Some(x) => println!("a[6] = {}", x),
        None => println!("error tho"),
    }

    for x in &a { println!("{}", x); }

    if let Some(x) = a.pop() {
        println!("{}", x);
    } // while let works too

}
fn main() {
    vectors();
}
