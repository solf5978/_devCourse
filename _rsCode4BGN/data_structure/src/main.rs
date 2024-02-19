
enum Direction {
    Left,
    Right,
}

fn main() {
    let next_move = Direction::Left;
    match next_move {
        Direction::Left => println!("go left"),
        Direction::Right => println!("go right"),
    }
}
