use std::io;

fn get_input() -> io::Result<String> {
    let mut buf = String::new();
    io::stdin().read_line(&mut buf)?;
    Ok(buf.trim().to_owned())
}

fn main() {
    let mut all_input = vec![];
    let mut times_input = 0;
    while times_input < 2 {
        match get_input() {
            Ok(words) => {
                all_input.push(words);
                times_input = times_input + 1;
            }
            Err(e) => println!("Error: {:?}", e),
        }
    }
    for input in all_input {
        println!(
            "Original: {:?}, Capitalized: {:?}",
            input,
            input.to_uppercase()
        );
    }
}
