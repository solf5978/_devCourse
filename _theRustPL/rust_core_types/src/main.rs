use std::mem;

fn main() {
    let unsigned_8b: u8 = 123;      // unsigned 8bits
    let unsigned_16b: u16 = 123;    // unsigned 16bits

    println!("8bits = {}", unsigned_8b);
    println!("16bits num = {}", unsigned_16b);

    //mutable value
    let mut mut_var: i8 = 0;
    println!("mutable var: {}", mut_var);
    mut_var = 15;
    println!("mutable var: {}", mut_var);

    println!("mut_var {}, size = {} bytes", mut_var, mem::size_of_val(&mut_var));


}
