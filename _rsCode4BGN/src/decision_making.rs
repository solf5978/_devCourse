fn main() {
    println!("Hello, world!");
    let my_bool = true;
    if my_bool == true {
        println!("hello");
    } else {
        println!("goodbye");
    }

    let n = 8;
    if n > 5 {
        println!(">5");
    } else if n < 5 {
        println!("<5");
    } else {
        println!("=5");
    }

    let some_bool = true;
    match some_bool {
        true => println!("its true"),
        false => println!("its false"),
    };

    let some_int = 3;
    match some_int {
        1 => println!("1"),
        2 => println!("2"),
        3 => println!("3"),
        _ => println!("Something else"),
    };

    let exercise_bool = true;
    if exercise_bool == true {
        println!("it's true");
    } else {
        println!("it's false");
    }

    match exercise_bool {
        true => println!("it's true"),
        false => println!("it's false"),
    };

    let match_int = 1;
    match match_int {
        1 => String::from("One"),
        2 => String::from("Two"),
        3 => String::from("Three"),
        _ => String::from("Not 1, 2 or 3"),
    };

    
}
