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

fn part_1() -> bool {
    maybe_access("admin").is_some()
}

fn part_2() -> Option<Access> {
    maybe_access("root").or_else(|| root())
}

fn part_3() -> Access {
    maybe_access("alice").unwrap_or_else(|| Access::Guest)
}

fn main() {
    let a: Option<i32> = Some(1);
    let a_is_some = a.is_some();
    let a_is_none = a.is_none();
    let a_mapped = a.map(|num| num + 1);
    let a_filtered = a.filter(|num| num == &1);
    let a_or_else = a.or_else(|| Some(5));
    let unwrapper = a.unwrap_or_else(|| 0);
}

#[cfg(test)]
mod test {
    use crate::*;
    #[test]
    fn chk_part_1() {
        assert_eq!(part_1(), true, "Admins have an access level");
    }
    #[test]
    fn chk_part_2() {
        assert_eq!(
            part_2(),
            Some(Access::Admin),
            "Root have admin access level"
        );
    }
    #[test]
    fn chk_part_3() {
        assert_eq!(part_3(), Access::Guest, "Guest User");
    }
}
