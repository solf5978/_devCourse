// -------------------------------------------
// 			Rust Ownership
// 			- Each value in Rust has a variable that’s called its owner.
// 			- There can be only one owner at a time.
// 			- When the owner goes out of scope, the value will be dropped.
// -------------------------------------------

fn main() {
    /*
    let mut x = 32.6;
    let mut y = x;

    println!("X: {}, y: {}", x, y);

    let s1 = String::from("abc");
    let s2 = &s1;
    println!("The value of s1 = {} and s2 = {}", s1, s2);
    */

    /*
    let vec1: Vec<i32> = vec![5, 6, 9, 8, 7];
    //let vec2 = vec1;
    // println!("Vec 1:  {:?}, Vec 2: {:?}", vec1, vec2);

    let vec2 = &vec1; // Referencing or borrowing
    println!("The first vector is {:?} {:?}", vec1, vec2);

    let vec2 = vec1.clone();
    println!("The first vector is {:?} {:?}", vec1, vec2);
    */

    {
        let my_name = String::from("Nouman Azam");
    }
    // println!("My name is {}", my_name);
}
