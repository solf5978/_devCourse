#[derive(Debug)]
struct Car {
    mpg: i8,
    color: String,
    top_speed: i16,
}

impl Car {
    fn new(mpg: i8, color: String, top_speed: i16) -> Self {
        Self {
            mpg,
            color,
            top_speed,
        }
    }
}

fn main() {
    let car1 = Car {
        mpg: 0,
        color: String::from("Red"),
        top_speed: 0,
    };

    println!("{:?}", car1);
}
