#[derive(Debug)]
enum Color {
    Black,
    Blue,
    Brown,
    Custom(String),
    Gray,
    Green,
    Purple,
    Red,
    White,
    Yellow,
}
#[derive(Debug)]
struct ShirtColor(Color);
impl ShirtColor {
    fn new(color: Color) -> Self {
        Self(color)
    }
}
#[derive(Debug)]
struct ShoeColor(Color);
impl ShoeColor {
    fn new(color: Color) -> Self {
        Self(color)
    }
}
#[derive(Debug)]
struct PantsColor(Color);
impl PantsColor {
    fn new(color: Color) -> Self {
        Self(color)
    }
}

fn print_shirt_color(color: ShirtColor) {
    println!("Shirt Color = {:?}", color);
}
fn print_shoe_color(color: ShoeColor) {
    println!("Shoes Color = {:?}", color);
}
fn print_pants_color(color: PantsColor) {
    println!("Pants Color = {:?}", color);
}
fn main() {
    let shirt_color = ShirtColor::new(Color::Gray);
    let pants_color = PantsColorColor::new(Color::Blue);
    let shoes_color = ShoeColorColor::new(Color::White);

    print_shirt_color(shirt_color);
    print_shoe_color(shoes_color);
    print_pants_color(pants_color);
}
