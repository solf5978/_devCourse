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
    format!("{first} {second}")
}

fn main() {}

#[cfg(test)]

mod test {
    use crate::*;
    #[test]
    fn check_clamp_lower() {
        let result = clamp(10, 100, 1000);
        let expected = 100;
        assert_eq!(result, expected, "Should be 100")
    }

    #[test]
    fn check_clamp_upper() {
        let result = clamp(2220, 100, 1000);
        let expected = 1000;
        assert_eq!(result, expected, "Should be 1000")
    }

    #[test]
    fn check_div() {
        let result = div(1, 1);
        let expected = Some(1);
        assert_eq!(result, expected, "Should be Some(1)")
    }

    #[test]
    fn check_concat() {
        let result = concat("a", "b");
        let expected = String::from("a b");
        assert_eq!(result, expected, "Should be a b")
    }
}
