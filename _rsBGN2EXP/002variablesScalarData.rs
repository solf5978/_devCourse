// --------------------------------------
// 			- Variables
// 			- Scalar Data Types
// --------------------------------------

fn main() {
    let mut x = 15;
    println!("The value of variable x = {}", x);

    x = 60.0;

    // --------------------------------------
    // 			Rules for naming variables
    // 			- Only letters, digits and underscores
    // 			- Should begin with letter or underscore
    // 			- Case Sensitive
    // --------------------------------------

    let x = 10;

    let y = 5 * 5;

    // --------------------------------------
    // 			Scalar Type
    //	 		- Integers
    //				- Signed
    //					- i8, i16, i32, i64
    //				- Unsigned
    //					- u8, u16,u32,u64
    // --------------------------------------

    println!("The Maximum number in i8 = {}", std::i8::MAX);
    println!("The Maximum number in u8 = {}", std::u8::MAX);

    // --------------------------------------
    // 			- Floats
    //				- f32, f64
    // --------------------------------------

    let z = 3.65;
    // let a = X + z;

    println!("The Maximum number in f32 = {}", std::f32::MAX);

    // --------------------------------------
    // 			- Boolean
    // --------------------------------------

    let status = false;
    println!(
        "The value of some of our variables are {:?}",
        (x, y, z, status)
    );

    let not_equals = 18 != 18;
    println!("The value of condition is 18! = 18 is {}", not_equals);

    // --------------------------------------
    // 			- Characters
    // 				- Represent single letters,
    //  			- digit,
    //				- emoji's or
    //				- unicode scalar values
    // --------------------------------------

    let c1 = 'a';
    let c2 = '3';
    let c3 = '+';
    let c4 = '\u{288A}';
    let c5 = '\"';
    println!(
        "The value of c1 is {}, c2 is {}, c3 is {}, c4 is {} and c5 is {}",
        c1, c2, c3, c4, c5
    );
}
