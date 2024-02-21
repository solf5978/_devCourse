use std::fmt::format;

fn strings() {
    let s:&'static str = "hello there!"; // &str -> string slice
    // cannot reassign
    for c in s.chars().rev() {
        println!("{}", c);
    }

    if let Some(first_char) = s.chars().nth(0) {
        println!("first letter is {}", first_char);
    }

    // string on heap
    let mut letters = String::new();
    let mut a = 'a' as u8;
    while a <= ('z' as u8) {
        letters.push(a as char);
        letters.push_str(",");
        a += 1;
    }

    println!("{}", letters);

    // &str <> string
    let u:&str = &letters;

    // concat string
    let z = letters + "abc";
    // let mut y = letters + &letters;
    let mut abc = String::from("hello world");
    let mut another_one = "hello world".to_string();
    another_one.remove(0);
    another_one.push_str("!!!!");
    println!("{}", another_one.replace("ello", "31j2o"));

    let name = "Dimitri";
    let greeting = format!("Hi, I'm {}, nice to meet you", name);
    println!("{}", greeting);

    let hello = "hello";
    let rust = "rust";
    let hello_rust = format!("{}, {}!", hello, rust);
    println!("{}", hello_rust);

    let run = "run";
    let forest = "forest";
    let rfr = format!("{0} {1} , {0}!", run, forest);
    println!("{}", rfr);

    let info = format!("the name's is {last}, {first} {last}.", first = "james", last = "bond");
    println!("{}", info);

    let mixed = format!(
        "{} {} {0} {} {data}",
        "a",
        "b",
        data = "hello",
    );
    println!("{}", mixed);

}

fn main() {
    println!("Hello, world!");
    strings();
}
