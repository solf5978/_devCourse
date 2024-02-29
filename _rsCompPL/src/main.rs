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

fn main() {}
