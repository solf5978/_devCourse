

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

    println!("is it {}"
             ,if temp > 20 {"hot"} else if temp < 10 {"cold"} else {"ok"});

    println!("it is {}", if temp > 20 {
        if temp > 30 {"super hot"} else {"just hot"}
        else if temp < 10 {{"cold"} else {"ok"}});
}

fn main() {
    if_statement();
}
