// --------------------------------------
//              Variables
//          	- Shadowing
//          	- Constants
// --------------------------------------

//
fn main() {
    let (first_number, second_number) = (250, 480.32);
    let large_number = 1_000_000;

    //let over_flow_number = 256;
    let x = 255;
    println!(
        "The value of the variable in octal is {:o} and in hexadecimal is {:X} and in binary {:b}",
        x, x, x
    );

    let n1 = 14;
    let n2 = 15.6;
    let n3 = n1 + n2 as i32; // late on n1 as f64
    println!("The value of n3 = {}", n3);

    // Shadowing

    let s = 5;
    let s = 5 * 5;
    println!("The value of the variable s = {}", s);

    let mut p = 5;
    let p = 5 * 5;

    //p = 60;
    let q = 32;
    let q = 'A';

    let mut r = 65;

    {
        r = 60;
        println!("Inside the code segment r: {}", r);
    }
    println!("Outside the code segment r: {}", r);

    const MAX_SALARY: u32 = 100_000;
}
