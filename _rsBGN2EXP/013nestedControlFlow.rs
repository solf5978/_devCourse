// -------------------------------------------
// 			- Nested If, if let and if let (in case of if else ladder)
// -------------------------------------------
fn main() {
    /* General Syntax

    if outer_condition {
        // Statement to execute if the outer_condition is true
        if inner_condition {
            // Statements to execute if both the outer and inner conditions are true
        } else {
            // some statements to execute
         }

     else {
         // some statements to execute
        }
    }
    */

    /*
    println!("Enter a Number");
    let mut some_num = String::new();
    std::io::stdin()
        .read_line(&mut some_num)
        .expect("failed to read input.");
    let some_num: i32 = some_num.trim().parse().expect("invalid input");

    if some_num != 0 {
        if some_num % 2 == 0 {
            println!("The number is even.");
        } else {
            println!("The number is odd.");
        }
    } else {
        println!("The number is 0 and it is neither even nor odd.");
    }
    */

    // if let
    /*
    let variable_name = if condition {
        // Statements to execute and
        // return value of variable without a semicolon
    } else {
        // Statements to execute and
        // value of variable of variable without a semicolon
    };  // semicolon
    */

    /*
    let value = if true { 1 } else { 2 };
    println!("Value = {}", value);
    */

    let marks = 95;

    let grade = if marks >= 90 {
        'A'
    } else if marks >= 80 {
        'B'
    } else if marks >= 70 {
        'C'
    } else if marks >= 60 {
        'D'
    } else {
        'F'
    };

    println!("The obtained grade is {:?}", grade);
}
