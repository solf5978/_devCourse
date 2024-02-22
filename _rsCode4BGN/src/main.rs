use std::io;

enum PowerState {
    Off,
    Sleep,
    Reboot,
    Shutdown,
    Hibernate,
}

impl PowerState {
    fn new(state: &str) -> Option<PowerState> {
        let state = state.trim().to_lowercase();
        match state.as_str() {
            "Off" => Some(PowerState::Off),
            "Sleep" => Some(PowerState::Sleep),
            "Reboot" => Some(PowerState::Reboot),
            "Shutdown" => Some(PowerState::Shutdown),
            "Hibernate" => Some(PowerState::Hibernate),
            _ => None,
        }
    }
}

fn print_power_action(state: PowerState) {
    use PowerState::*;
    match state {
        Off => println!("Turing Off..."),
        Sleep => println!("Sleep..."),
        Reboot => println!("Restarting..."),
        Shutdown => println!("Shutting Down..."),
        Hibernate => println!("Hibernated..."),
    }
}
fn get_input() -> io::Result<String> {
    let mut buf = String::new();
    io::stdin().read_line(&mut buf)?;
    Ok(buf.trim().to_owned())
}

fn main() {
    let mut buffer = String::new();
    let user_input_status = io::stdin().read_line(&mut buffer);
    if user_input_status.is_ok() {
        match PowerState::new(&buffer) {
            Some(state) => print_power_action(state),
            None => println!("Invalide Power State"),
        }
    } else {
        println!("Error reading Input");
    }

    let mut all_input = vec![];
    let mut times_input = 0;
    while times_input < 2 {
        match get_input() {
            Ok(words) => {
                all_input.push(words);
                times_input = times_input + 1;
            }
            Err(e) => println!("Error: {:?}", e),
        }
    }
    for input in all_input {
        println!(
            "Original: {:?}, Capitalized: {:?}",
            input,
            input.to_uppercase()
        );
    }
}
