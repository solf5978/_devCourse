
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

enum Flavor {
    Sparkling,
    Sweet,
    Fruity,
}

struct Drink {
    flavor : Flavor,
    fluid_oz: f64,
}

fn print_color(my_color: Color) -> String {
    match my_color {
        Color::Red => "Red".to_string(),
        Color::Yellow => "小黃雞".to_string(),
        Color::Blue => "Blue".to_string(),

    }
}

fn pDrink(drink: Drink) {
    match drink.flavor {
        Flavor::Sparkling => println!("sparkling"),
        Flavor::Fruity => println!("fruity"),
        Flavor::Sweet => println!("sweet"),
    };
    println!("oz : {:?}", drink.fluid_oz);
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

    let sweet = Drink {
        flavor: Flavor::Sweet,
        fluid_oz: 6.0,
    };

    pDrink(sweet);
}
