enum Color {
    Red,
    Purple,
    Yellow,
}

fn color_match(input: Color) {
    match input {
        Color::Red => println("It's red"),
        Color::Purple => println("It's Purple"),
        Color::Yellow => println("It's Yellow"),
        _ => println("Error with input color"),
    }
}

fn main() {
    color_match(Color::Red);
}
