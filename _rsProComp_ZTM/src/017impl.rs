enum BoxColor {
    Brown,
    Red,
}

impl BoxColor {
    fn print(&self) {
        match self {
            BoxColor::Brown => println!("brown"),
            BoxColor::Red => println!("Red"),
        }
    }
}
struct Dimensions {
    width: f64,
    height: f64,
    depth: f64,
}

impl Dimensions {
    fn print(&self) {
        println!("width: {:?}", self.width);
        println!("width: {:?}", self.height);
        println!("width: {:?}", self.depth);
    }
}

struct ShipBox {
    color: BoxColor,
    weight: f64,
    dimensions: Dimensions,
}

impl ShipBox {
    fn new(weight: f64, color: BoxColor, dimensions: Dimensions) -> Self {
        Self {
            color,
            weight,
            dimensions,
        }
    }
    fn print(&self) {
        self.color.print();
        self.dimensions.print();
        println!("weight: {:?}", self.weight);
    }
}

fn main() {
    let small_dimentsions = Dimensions {
        width: 1.0,
        height: 2.0,
        depth: 3.0,
    };

    let new_box = ShipBox {
        weight: 0.35,
        color: BoxColor::Red,
        dimensions: Dimensions {
            width: 0.5,
            height: 2.0,
            depth: 1.5,
        },
    };

    let new_box_2 = ShipBox::new(0.53, BoxColor::Brown, small_dimentsions);

    new_box.print();
    new_box_2.print();
}
