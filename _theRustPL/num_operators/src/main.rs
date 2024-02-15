fn main() {
    let mut a = 2 + 3 * 4;
    println!("{}", a);
    a = a + 1;
    a -= 2;
    a += 5;

    println!("remainder of {} / {} = {}", a, 3, (a%3));

    let a_cubed = i32::pow(a, 3);
    println!("{} cubed is {}", a, a_cubed);

}
