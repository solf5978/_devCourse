
enum Direction {
    Left,
    Right,
    Up,
}

enum Color {
    Red,
    Yellow,
    Blue,
}

fn print_color(my_color: Color) -> String {
    match my_color {
        Color::Red => "Red".to_string(),
        Color::Yellow => "小黃雞".to_string(),
        Color::Blue => "Blue".to_string(),

    }
}

fn main() {
    let next_move = Direction::Left;
    match next_move {
        Direction::Left => println!("go left"),
        Direction::Right => println!("go right"),
        Direction::Up =>println!("go up"),

    }
    let output = print_color(Color::Yellow);
    println!("{}", output);
}
