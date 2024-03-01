#[derive(Debug)]
struct Car {
    mpg: i8,
    color: String,
    top_speed: i16,
}

#[derive(Debug)]
struct MotoCycle {
    mpg: i8,
    color: String,
    top_speed: i16,
}

pub trait Properties {
    fn set_mpg(&mut self, mpg: i8);
    fn set_color(&mut self, color: String);
    fn set_top_speed(&mut self, top_speed: i16);
}

impl Properties for MotoCycle {
    fn set_mpg(&mut self, mpg: i8) {
        self.mpg = mpg;
    }
    fn set_color(&mut self, color: String) {
        self.color = color;
    }
    fn set_top_speed(&mut self, top_speed: i16) {
        self.top_speed = top_speed;
    }
}

impl Properties for Car {
    fn set_mpg(&mut self, mpg: i8) {
        self.mpg = mpg;
    }
    fn set_color(&mut self, color: String) {
        self.color = color;
    }
    fn set_top_speed(&mut self, top_speed: i16) {
        self.top_speed = top_speed;
    }
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
