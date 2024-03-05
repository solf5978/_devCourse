use std::sync::OnceState;

enum PowerStates {
    Off,
    Sleep,
    Reboot,
    Shutdown,
    Hibernate,
}

impl PowerStates {
    fn new(state: &str) -> Option<PowerStates> {
        let state = state.trim().to_lowercase();
        match state.as_str() {
            "off" => Some(PowerStates::Off),
            "sleep" => Some(PowerStates::Sleep),
            "reboot" => Some(PowerStates::Reboot),
            "shutdown" => Some(PowerStates::Shutdown),
            "hibernate" => Some(PowerStates::Hibernate),
            _ => None,
        }
    }
}

fn current_power_state(state: PowerStates) {
    use PowerStates::*;
    match state {
        Off => println!("Power Off"),
        Sleep => println!("Sleeping"),
        Reboot => println!("Rebooting"),
        Shutdown => println!("Shutting Down"),
        Hibernate => println!("Hibernating"),
    }
}

fn main() {
    let mut buffer = String::new();
    let user_input_status = std::io::stdin().read_line(&mut buffer);
    if user_input_status.is_ok() {
        match PowerStates::new(&buffer) {
            Some(state) => current_power_state(state),
            None => println!("Invalid Power State Code"),
        }
    } else {
        println!("Error Reading Input");
    }
}
