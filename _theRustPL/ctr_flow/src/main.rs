

fn if_statement()
{
    let temp = 25;
    if temp > 30
    {
        println!("It's hot outside");
    } else if temp < 10 {
        println!("It's cold ");
    } else {
        println!("It's a mild weather");
    }

    // if else is an expression
    let day:str = if temp > 20 {"sunny"} else {"cloudy"};
    println!("today is {}", day);
}

fn main() {
    if_statement();
}
