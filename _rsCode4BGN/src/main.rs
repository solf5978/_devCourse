use std::{error, result};

use thiserror::Error;
#[derive(Debug, Eq, PartialEq)]
enum Access {
    Admin,
    User,
    Guest,
}

enum ProgramError {}
#[derive(Debug, Error)]
enum MenuError {
    #[error("menu item not found")]
    NotFound,
}

#[derive(Debug, Error)]
enum MathError {
    #[error("divide by zero error")]
    DivideByZero,
}

fn pick_menu(choice: &str) -> Result<i32, MenuError> {
    match choice {
        "1" => Ok(1),
        "2" => Ok(2),
        "3" => Ok(3),
        _ => Err(MenuError::NotFound),
    }
}

fn divide(a: i32, b: i32) -> Result<i32, MathError> {
    if b != 0 {
        Ok(a / b)
    } else {
        Err(MathError::DivideByZero)
    }
}

fn run(step: i32) -> Result<(), ProgramError> {
    if step == 1 {
        pick_menu("4")?;
    } else if step == 2 {
        divide(1, 0)?;
    }
    Ok(())
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

trait Perimeter {
    fn calculate_peri(&self) -> i32;
}
struct Square {
    side: i32,
}

impl Perimeter for Square {
    fn calculate_peri(&self) -> i32 {
        self.side * 4
    }
}
struct Triangle {
    side_a: i32,
    side_b: i32,
    side_c: i32,
}
impl Perimeter for Triangle {
    fn calculate_peri(&self) -> i32 {
        self.side_a + self.side_b + self.side_c
    }
}
fn print_perimeter(shape: impl Perimeter) {
    let peri = shape.calculate_peri();
    println!("peri-> {:?}", peri);
}

fn main() {
    println!("{:?}", run(1));
    println!("{:?}", run(2));
    let square = Square { side: 5 };
    let triangle = Triangle {
        side_a: 2,
        side_b: 3,
        side_c: 4,
    };
    print_perimeter(square);
    print_perimeter(triangle);

    let data: Vec<_> = vec![1, 2, 3, 4, 5]
        .iter()
        .map(|num| num * 3)
        .filter(|num| num > &10)
        .collect();
    println!("{:?}", data);

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
