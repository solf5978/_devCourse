struct Survey {
    q1: Option<i32>,
    q2: Option<bool>,
    q3: Option<String>,
}

struct Student {
    name: String,
    locker: Option<i32>,
}

fn main() {
    let mary = Student {
        name: "Mary".to_owned(),
        locker: Some(3),
    };

    println!("student: {:?}", mary.name);
    match mary.locker {
        Some(num) => println!("locker number -> {:?}", num),
        None => println!("no locker assigned"),
    }


    println!("Hello, world!");
    let rep = Survey {
        q1: Some(12),
        q2: Some(true),
        q3: Some("A".to_owned()),
    };

    match rep.q1 {
        Some(ans) => println!("q1: {:?}", ans),
        None => println!("q1: No rep"),
    }

    match rep.q2 {
        Some(ans) => println!("q1: {:?}", ans),
        None => println!("q2: No rep"),
    }

    match rep.q3 {
        Some(ans) => println!("q1: {:?}", ans),
        None => println!("q3: No rep"),
    }
}
