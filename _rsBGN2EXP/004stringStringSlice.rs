// -------------------------------------------------
// 			Strings
// 			 - Fixed length strings (&str)
// 			 - Growable strings (String)
// -------------------------------------------------

fn main() {
    let some_string = "Fixed length string";

    let mut growable_string = String::from("This string will grow");
    println!("The string is: \"{}\" ", growable_string);

    growable_string.push('s');
    println!("The string is: \"{}\"", growable_string);

    growable_string.pop();
    println!("The string is: \"{}\" ", growable_string);

    growable_string.push_str(" which i will use");
    println!("The string is \"{}\" ", growable_string);

    println!(
        "Basic functions on Strings,
        is_emtpy(): {}, 
        length(): {},
        Bytes(): {}, 
        Contains use: {},",
        growable_string.is_empty(),
        growable_string.len(),
        growable_string.capacity(),
        growable_string.contains("use")
    );

    growable_string.push_str("   ");
    let str_len = growable_string.trim().len();

    let number = 6;
    let num_str = number.to_string();
    println!("Is the number a string: {}", number.to_string() == "6");

    let some_char = 'a';
    let char_str = some_char.to_string();

    let my_name = "Nouman".to_string();

    let empty_string = String::new();
    println!("Length is: {}", empty_string.len());

    let s_1 = "Nouman".to_string();
    let s_2 = "Azam".to_string();
    let s_3 = format!("My first name is {}, and my last name is {}", s_1, s_2);
    println!("{}", s_3);

    let concat = format!("{}{}", s_1, s_2);
}
