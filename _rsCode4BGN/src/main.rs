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

fn clamp(n: i32, lower: i32, upper: i32) -> i32 {
    if n < lower {
        lower
    } else if n > upper {
        upper
    } else {
        n
    }
}

fn div(a: i32, b: i32) -> Option<i32> {
    Some(a / b)
}
fn concat(first: &str, second: &str) -> String {
    format!("{} {}", first, second)
}
fn main() {
    let add = |a: i32, b: i32| -> i32 { a + b };
    let add = |a, b| a + b;
    let sum = add(1, 1);

    let user_name = "sam";
    let user = find_user(user_name).map(|user_id| User {
        user_id,
        name: user_name.to_owned(),
    });
    match user {
        Some(user) => println!("{:?}", user),
        None => println!("user not found"),
    }
}

#[cfg(test)]
mod test {
    use crate::*;
    #[test]
    fn clamp_lower() {
        let result = clamp(10, 100, 1000);
        let expected = 100;
        assert_eq!(result, expected, "shoudld be 100");
    }

    #[test]
    fn clamp_upper() {
        let result = clamp(100000, 100, 1000);
        let expected = 1000;
        assert_eq!(result, expected, "shoudld be 1000");
    }

    #[test]
    fn check_div() {
        let result = div(1, 1);
        let expected = Some(1);
        assert_eq!(result, expected, "should be 1");
    }

    #[test]
    fn check_concat() {
        let result = concat("a", "b");
        let expected = String::from("a b");
        assert_eq!(result, expected, "should be a b");
    }
}
