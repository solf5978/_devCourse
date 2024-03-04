enum Flavor {
    Sparkling,
    Sweet,
    Fruity,
}

struct Beverage {
    flavor: Flavor,
    fluid_oz: f64,
}

fn print_drink(drink: Beverage) {
    match drink.flavor {
        Flavor::Sparkling => println!("spakrling"),
        Flavor::Sweet => println!("sweet"),
        Flavor::Fruity => println!("fruity"),
    }
    println!("oz: {:?}", drink.fluid_oz);
}

fn main() {
    let first_drink = Beverage {
        flavor: Flavor::Sweet,
        fluid_oz: 6.0,
    };

    print_drink(first_drink);
}
