trait Body {}

trait Color {}
#[derive(Debug)]
struct Vehicle<T, U>
where
    T: Body,
    U: Color,
{
    body: T,
    color: U,
}

impl<T: Body, U: Color> Vehicle<T, U> {
    pub fn new(body: T, color: U) -> Self {
        Self { body, color }
    }
}
#[derive(Debug)]
struct Car;
impl Body for Car {}
#[derive(Debug)]
struct Truck;
impl Body for Truck {}
#[derive(Debug)]
struct Red;
impl Color for Red {}
#[derive(Debug)]
struct Blue;
impl Color for Blue {}

fn main() {
    let red_truck = Vehicle::new(Truck, Red);
    let blue_car = Vehicle::new(Car, Blue);
    println!("{:?}", red_truck);
    println!("{:?}", blue_car);
}
