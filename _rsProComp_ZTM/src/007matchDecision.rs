fn main() {
    let my_name = "Bob";
    match my_name {
        "Bob" => println!("Hello bob"),
        "Hel" => println!("Hello bob"),
        "Hela" => println!("Hello bob"),
        "Helb" => println!("Hello bob"),
        _ => println!("Who are you"),
    }
}
