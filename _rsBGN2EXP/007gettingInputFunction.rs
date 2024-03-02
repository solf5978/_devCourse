// -------------------------------------------------
// 			- Functions
// 			- Inputs
// -------------------------------------------------
fn main() {
    basic_fn();

    function_with_inputs("Nouman", 40_000);

    let full_name = "Kamran";
    let salary_info = 50_000;
    function_with_inputs(full_name, salary_info);

    let answer = function_with_inputs_outputs(10, 15);
    println!("The answer of multiplicatin is {}", answer);

    let (multiplication, addition, subtraction) = function_with_inputs_multiple_outputs(10, 15);
    println!(
        "Multiplication = {}, Addition = {}, Subtraction = {}",
        multiplication, addition, subtraction
    );

    let result = function_with_inputs_multiple_outputs(10, 15);

    let full_name = {
        let first_name = "Nouman";
        let last_name = "Azam";
        format!("{} {}", first_name, last_name)
    };

    println!("My full name is {}", full_name);

    let mut n = String::new();
    std::io::stdin()
        .read_line(&mut n)
        .expect("failed to read input.");

    let n: f64 = n.trim().parse().expect("invalid input");

    println!("{:?}", n);
}

fn basic_fn() {
    println!("This is a basic function");
}

fn function_with_inputs(name: &str, salary: i32) {
    println!("The name is {} and the salary is {}", name, salary);
}

fn function_with_inputs_outputs(num1: i32, num2: i32) -> i32 {
    num1 * num2
}

fn function_with_inputs_multiple_outputs(num1: i32, num2: i32) -> (i32, i32, i32) {
    (num1 * num2, num1 + num2, num1 - num2) // changing this to an expression by adding a semicolon will return an error
}
