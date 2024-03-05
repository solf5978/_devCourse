#[derive(Debug, Eq, PartialEq)]
enum Access {
    Admin,
    User,
    Guest,
}

fn maybe_access(name: &str) -> Option<Access> {
    match name {
        "admin" => Some(Access::Admin),
        "gary" => Some(Access::User),
        _ => None,
    }
}

fn root() -> Option<Access> {
    Some(Access::Admin)
}

fn part1() -> bool {
    maybe_access("admin").is_some()
}

fn part2() -> Option<Access> {
    maybe_access("root").or_else(|| root())
}

fn part3() -> Access {
    maybe_access("Alice").unwrap_or_else(|| Access::Guest)
}

fn main() {}

#[cfg(test)]
mod test {
    use crate::*;

    #[test]
    fn check_part_1() {
        assert_eq!(part1(), true, "Admins have an access level");
    }

    #[test]
    fn check_part_2() {
        assert_eq!(part2(), Some(Access::Admin), "Roots have an access level");
    }

    #[test]
    fn check_part_3() {
        assert_eq!(part3(), Access::Guest, "Guest User");
    }
}
