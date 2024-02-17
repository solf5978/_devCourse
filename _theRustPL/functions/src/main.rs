
fn print_value( input: i32) {
    println!("Value = {}", input);
}

fn increase(input: &mut i32) {
    *input += 1;
}

fn product(in1: i32, in2: i32) -> i32 {
    in1 * in2
}
fn functions() {
    print_value(33);
    let mut z = 1;
    increase(&mut z);
    println!("z -> {}", z);

    let p = product(33, 20);
    println!("p -> {} ", p);
}

fn main() {
    println!("Hello, world!");

    functions();
}
