use std::mem;

fn main() {
    let var_u8: u8 = 0;
    let var_u16: u16 = 0;
    let var_u32: u32 = 0;
    let var_u64: u64 = 0;
    let var_i8: i8= 0;
    let var_i16: i16 = 0;
    let var_i32: i32 = 0;
    let var_i64: i64 = 0;

    println!(" u8's value = {} , and its size is {}", var_u8, mem::size_of_val(&var_u8));
    println!(" u16's value = {} , and its size is {}", var_u16, mem::size_of_val(&var_u16));
    println!(" u32's value = {} , and its size is {}", var_u32, mem::size_of_val(&var_u32));
    println!(" u64's value = {} , and its size is {}", var_u64, mem::size_of_val(&var_u64));
    println!(" i8's value = {} , and its size is {}", var_i8, mem::size_of_val(&var_i8));
    println!(" i16's value = {} , and its size is {}", var_i16, mem::size_of_val(&var_i16));
    println!(" i32's value = {} , and its size is {}", var_i32, mem::size_of_val(&var_i32));
    println!(" i64's value = {} , and its size is {}", var_i64, mem::size_of_val(&var_i64));
    





}
