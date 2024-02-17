
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

fn main() {
    println!("Hello, world!");

    functions();
}
