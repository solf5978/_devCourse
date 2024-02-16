use std::collections::HashMap;

fn vectors() {
    let mut a = Vec::new();
    a.push(1);
    a.push(2);
    a.push(3);

    println!("a = {:?}", a);

    a.push(44);
    println!("a = {:?}", a);
    println!("a[0] = {}", a[0]);

    let idx: usize = 0;
    a[idx] = 312;
    println!("a[0] = {}", a[idx]);

    match a.get(6) {
        Some(x) => println!("a[6] = {}", x),
        None => println!("error tho"),
    }

    for x in &a { println!("{}", x); }

    if let Some(x) = a.pop() {
        println!("{}", x);
    } // while let works too
}

fn create_hashmap() {
    let mut shapes = HashMap::new();
    shapes.insert(String::from("triangle"), 3);
    shapes.insert(String::from("square"), 4);

    println!("a square has {} sides", shapes["square".into()]);

    for (k, v) in &shapes {
        println!("{} : {}", k, v);
    }

    println!("{:?}", shapes);

    shapes.entry("circle".into()).or_insert(1);
    {
        let actual = shapes.entry("circle".into()).or_insert(1);
        *actual = 0;
    }

    println!("{:?}", shapes);
}

fn main() {
    vectors();
    create_hashmap();
    create_hsahset();
}
