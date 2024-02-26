use crate::Colors::Red;

#[allow(unused_variables)]
#[allow(unused_assignments)]

fn main() {
    let p1: Point<i32> = Point {X: 6, Y: 8};
    let p2: Point<f64> = Point {X: 3.25, Y: 8.63};
    println!("{:?}", p1);
    println!("{:?}", p2);

    let c1 = Red("#f00");
    let c2 = Red(255);
    println!("{:?}", c1);
    println!("{:?}", c2);

    let p3: Point2<i32, f64> = Point2 {x: 34, y: 8.5};
    println!("{:?}", p3);
}

#[derive(Debug)]
struct Point<T> {
    X: T,
    Y: T
}

#[derive(Debug)]
enum Colors<T> {
    Red(T),
    Blue(T),
    Green(T)
}

#[derive(Debug)]
struct Point2<T, V> {
    x: T,
    y: V
}