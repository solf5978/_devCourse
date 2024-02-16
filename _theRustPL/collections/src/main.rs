
fn vectors() {
    let mut a = Vec::new();
    a.push(1);
    a.push(2);
    a.push(3);

    println!("a = {:?}", a);

    a.push(44);
    println!("a = {:?}", a);
    println!("a[0] = {}", a[0]);

    let idx: usize = 12;
    a[idx] = 312;
    println!("a[0] = {}", a[idx]);

}
fn main() {
    vectors();
}
