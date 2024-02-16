use std::mem;

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
    RGBColor(u8, u8, u8),
    Cmyk {
        cyan: u8, magenta: u8, yellow: u8, black: u8
    },

}

fn enums() {
    let c:Color = Color::Red;
    let cmyk:Color = Color::Cmyk {cyan: 9, magenta: 128, yellow: 0, black: 0};

    match c {
        Color::Red => println!("RED COLOR"),
        Color::Green => println!("GREEN COLOR"),
        Color::Blue => println!("BLUE COLOR"),
        Color::RGBColor(r, g ,b ) => println!("RGB({}, {} {})", r, g, b),
        Color::Cmyk {cyan:_, magenta:_, yellow:_, black:_} => println!("cmyk"),
        _ => println!("exhaustive"),
    }
}

union IntOrFloat {
    i: i32,
    f: f32,
}

union IntOrFloat64 {
    i: i64,
    f: f64,
}

fn process_value(iof: IntOrFloat) {
    unsafe {
        match iof {
            IntOrFloat { i:42 } => {
                println!("meaning of life value");
            }
            IntOrFloat { f  } => {
                println!("value = {}", f)
            }
        }
    }
}

fn create_array() {
    let mut a:[i32;5] = [1, 2, 3, 4, 5,];
    println!("a has {} elements, first is {}",
        a.len(), a[0]);
    a[0] = 321;
    println!("first element of a is -> {}", a[0]);

    println!("{:?}", a);

    if a != [1, 2, 3, 4, 5] {
        println!("mismatch");
    }

    let b = [1u8; 10]; //having 10 elements with value of 1
    for i in 0..b.len() {
        println!("{}", b[i]);
    }

    println!("b took up {} bytes", mem::size_of_val(&b));

    let mtx:[[f32;3]; 2] = [
        [1.0, 0.0, 0.0],
        [0.0, 2.0, 0.0]
    ];
    println!("{:?}", mtx);

}

fn main() {
    structures();
    println!("Hello, world!");

    let mut iof = IntOrFloat { i: 123 };
    iof.i = 234;

    let value = unsafe { iof.i };
    println!("iof.i = {}", value);
    process_value(IntOrFloat { i: 42 });

    let first: f64= 3.0;
    let second: f64 = 2.5;
    let result =
        if second != 0.0 { Some(first/second)} else { None };
    match result {
        Some(z) => println!("{}/{}={}", first, second, z),
        None => println!("cannot divide by zero")
    }
    // Option -> Some(v) | None
    if let Some(z) = result {
        println!("result = {}", z)
    }

    create_array();
}
