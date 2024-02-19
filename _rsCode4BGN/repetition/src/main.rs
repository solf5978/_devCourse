fn main() {
    println!("Hello, world!");
    loop {
        println!("hello");
        break;
    }

    loop { 
        let mut i = 3;
        loop {
            println!("{:?}", i);
            i = i - 1;
            if i == 0 { break; }
        }
    }

    let mut rep = 1;
    while rep <= 3 {
        println!("{:?}", rep);
        rep = rep + 1;
    }
}