#[allow(unused_variables)]
#[allow(unused_assignments)]

fn main() {
    let a = |a: i32| a+1;
    println!("{}", a(6));
    let b = |b: i32| {
        let c = b + 1;
        c
    };
    println!("{}", b(4));

    let gen = |x| println!("{}", x);
    gen(3);
    // gen(true);
}