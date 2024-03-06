use thiserror::Error;
enum ProgramError {}

#[derive(Debug, Error)]
enum MenuError {
    #[error("menu item not found")]
    NotFound,
}

#[derive(Debug, Error)]
enum MathError {
    #[error("divide by zero error")]
    DividedByZero,
}

fn pick_menu(choice: &str) -> Result<i32, MenuError> {
    match choice {
        "1" => Ok(1),
        "2" => Ok(2),
        "3" => Ok(3),
        _ => Err(MenuError::NotFound),
    }
}
