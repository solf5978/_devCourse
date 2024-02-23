fn add_fn(a: i32, b: i32) -> i32 {
    a + b
}

#[derive(Debug)]
struct User {
    user_id: i32,
    name: String,
}

fn find_user(name: &str) -> Option<i32> {
    let name = name.to_lowercase();
    match name.as_str() {
        "sam" => Some(1),
        "matt" => Some(2),
        "katie" => Some(9),
        _ => None,
    }
}
fn main() {
    let add = |a: i32, b: i32| -> i32 { a + b };
    let add = |a, b| a + b;
    let sum = add(1, 1);
}
