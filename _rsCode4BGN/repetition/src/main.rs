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
}
