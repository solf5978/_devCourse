trait Perimeter {
    fn calculate_perimeter(&self) -> i32;
}

struct Square {
    side: i32,
}

impl Perimeter for Square {
    fn calculate_perimeter(&self) -> i32 {
        self.side * 4
    }
}

struct Triangle {
    side_one: i32,
    side_two: i32,
    side_three: i32,
}

impl Perimeter for Triangle {
    fn calculate_perimeter(&self) -> i32 {
        self.side_one + self.side_two + self.side_three
    }
}

fn print_perimeter(shape: impl Perimeter) {
    let peri = shape.calculate_perimeter();
    println!("Perimeter -> {peri:?}");
}

fn main() {
    let square = Square { side: 5 };
    let triangle = Triangle {
        side_one: 1,
        side_two: 2,
        side_three: 3,
    };

    print_perimeter(square);
    print_perimeter(triangle);
}
