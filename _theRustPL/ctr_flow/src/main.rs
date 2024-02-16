

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
    let day = if temp > 20 {"sunny"} else {"cloudy"};
    println!("today is {}", day);

    println!("is it {}"
             ,if temp > 20 {"hot"} else if temp < 10 {"cold"} else {"ok"});

    println!("it is {}", if temp > 20 {
        if temp > 30 {"super hot"} else {"just hot"}}
        else if temp < 10 {"cold"} else {"ok"});
}

fn while_loop() {
    let mut x = 1;

    while x < 1000 {
        x *=2 ;
        if x == 64 { continue; }
        println!("x's value = {}", x);

        if x == 1024 { break; }
    }

    let mut y:i32 = 1;
    loop {
        y *= 2;
        println!("y = {}", y);
        if y == 1 << 10 { break; } // break @ 1024
    }
}

fn for_loop() {
    for i in 1..11 {
        if i == 3 { continue; }

        if i == 8 { break; }
        println!("current value is = {}", i);
    }

    for (idx, pos_y) in (30..41).enumerate() {
        println!("{} and {} ", idx, pos_y);
    }
}

fn main() {
    if_statement();
    while_loop();
    for_loop();
}
