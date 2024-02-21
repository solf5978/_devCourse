struct Survey {
    q1: Option<i32>,
    q2: Option<bool>,
    q3: Option<String>,
}

fn main() {
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
}
