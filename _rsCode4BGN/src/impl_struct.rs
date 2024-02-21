
enum Color {
    Brown,
    Red,
}

impl Color {
    fn print(&self) {
        match self {
            Color::Brown => println!("BROWN"),
            Color::Red => println!("RED"),
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
        println!("Width: {:?}", self.width);
        println!("Height: {:?}", self.height);
        println!("Depth: {:?}", self.depth);
    }
}

struct ShippingBox {
    color: Color,
    weight: f64,
    dimensions: Dimensions,
}

impl ShippingBox {
    fn new(weight: f64, color: Color, dimensions: Dimensions) -> Self {
        Self {
            weight,
            color,
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
    println!("Hello, world!");
    let parcel_s = Dimensions {
        width: 1.0,
        height: 2.0,
        depth: 3.0,
    };

    let parcel_s = ShippingBox::new(5.0, Color::Red, parcel_s);
    parcel_s.print();

}
