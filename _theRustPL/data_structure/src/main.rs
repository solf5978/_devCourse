
struct Point {
    x : f64,
    y : f64,
}

struct Line {
    start: Point,
    end: Point,
}

fn structures() {
    let p = Point { x: 3.0, y: 4.0 };
    println!("point p is at ({} , {})", p.x, p.y);

    let p2 = Point { x: 5.0, y: 10.0 };
    let my_line = Line { start: p, end: p2 };
}

enum Color {
    Red,
    Green,
    Blue,
    RGBColor(u8, u8, u8)
}

fn enums() {
    let c:Color = Color::Red;

    match c {
        Color::Red => println!("RED COLOR"),
        Color::Green => println!("GREEN COLOR"),
        Color::Blue => println!("BLUE COLOR"),
        _ => println!("exhaustive"),
    }
}

fn main() {
    structures();
    println!("Hello, world!");
}
