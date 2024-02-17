
struct Point {
    x: f64,
    y: f64,
}

struct Line {
    start: Point,
    end: Point
}

impl Line {
    fn len(&self) -> f64 {
        let dx = self.start.x - self.end.x;
        let dy = self.start.y - self.end.y;
        return (dx * dx + dy * dy).sqrt()
    }
}


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

fn say_hello() { println!("hello"); }
fn closures() {
    say_hello();
    let haha = say_hello;
    haha();

    let plus_one = |x: i32| -> i32 { x + 1 };
    let a = 6;
    println!("{} + 1 = {}", a, plus_one(a));

    let plus_two = |x| {
        let mut z = x;
        z += 2;
        z
    }; println!("{}  + 2 = {}", 3, plus_two(3));

    let plus_three = |x:&mut i32| *x += 3;
    let mut f = 12;
    plus_three(&mut f);
    println!("f = {}", f);
}

fn is_even(x: u32) -> bool {
    x % 2 ==0
}

fn main() {
    println!("Hello, world!");

    functions();
    closures();
    let limit = 500;
    let mut sum = 0;

    let above_limit = |y| y > limit;
    for i in 0.. {
        let isq = i * i;

        if above_limit(isq) {
            break;
        } else if is_even(isq) {
            sum += isq;
        }
    }
    println!("final result -> {}", sum);
}
