// --------------------------------------
// 			- Program Ouputs
// 			- Comments and its Different Styles
// --------------------------------------

fn main() {
    // This is our first program in this course
    // This is the second line of comment

    /*
    This is
    a
    multi-line
    comment
     */

    println!("Hello from Rust");

    print!("Hello World");

    //print!(10);

    println!("The value is {}", 10);

    println!(
        "My first name is {} and my last name is {}",
        "Nouman", "Azam"
    );

    print!("This is a print command");

    print!("This is going to be printed on the same line");
    print!("This is going to be printed on the same line");
    print!("This is going to be printed on the same line");

    print!(
        "This is going to be 
                printed on multiple 
                lines"
    );

    println!("\n\n This is going to be printed after a line");

    println!("\t This will have some empty space at the begining");

    print!(
        "This is some text which will be overwritten \r This text will only appear on the screen"
    );

    println!("\\n\n The first slash n will have no effect");

    println!("This will print single quote \' and this double quotes \"");

    println!("This will print one back slash \\");

    println!(
        "I am doing {2} from {1} years and i {0} it",
        "like", 20, "programming"
    );

    println!(
        "{language} is a system programming language which is cool to {activity} in.",
        language = "Rust",
        activity = "code"
    );

    println!("The summation of 25 +10 = {}", 25 + 10);
}
