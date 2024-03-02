// -------------------------------------------
// 		        - String Concatenation and Ownership
// -------------------------------------------
fn main() {
    /*
    let s1 = String::from("hello");
    let s2: &str = "world";

    let s3 = s1 + s2; // the ownership changed here
    println!("{}", s3);
    */

    /*
    let s1 = String::from("hello");
    let s2 = String::from("world");

    let s3 = s1 + &s2;
    println!("{} {} ", s3, s2);
    */

    let s1 = String::from("hello");
    let s2 = String::from("world");
    let s3 = String::from(" from Rust");

    let s4 = s1 + &s2 + &s3;
    println!("{} {} {}", s4, s2, s3);
}
