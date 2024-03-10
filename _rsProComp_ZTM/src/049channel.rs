use colored::Colorize;
use crossbeam_channel::{unbounded, Receiver};
use std::thread::{self, JoinHandle};

enum LightMsg {
    ChangeColor(u8, u8, u8),
    Disconnect,
    Off,
    On,
}

enum LightStatus {
    Off,
    On,
}

fn spawn_light_thread(receiver: Receiver<LightMsg>) -> JoinHandle<LightStatus> {
    thread::spawn(move || {
        let mut light_status = LightStatus::Off;
        loop {
            if let Ok(msg) = receiver.recv() {
                match msg {
                    LightMsg::ChangeColor(r, g, b) => {
                        println!("Color changed to : {}", "        ".on_truecolor(r, g, b));
                        match light_status {
                            LightStatus::Off => println!("Light Off"),
                            LightStatus::On => println!("Light On"),
                        }
                    }
                    LightMsg::On => {
                        println!("Turned Light on");
                        light_status = LightStatus::On;
                    }
                    LightMsg::Off => {
                        println!("Turned Light on");
                        light_status = LightStatus::Off;
                    }
                    LightMsg::Disconnect => {
                        println!("Disconnecting...");
                        light_status = LightStatus::Off;
                        break;
                    }
                }
            } else {
                println!("channel disconnected");
                light_status = LightStatus::Off;
                break;
            }
        }
        light_status
    })
}

fn main() {
    let (s, r) = unbounded();
    let light = spawn_light_thread(r);
    s.send(LightMsg::On);
    s.send(LightMsg::ChangeColor(255, 0, 0));
    s.send(LightMsg::ChangeColor(0, 255, 0));
    s.send(LightMsg::ChangeColor(0, 0, 255));
    s.send(LightMsg::Off);
    s.send(LightMsg::Disconnect);

    let light_status = light.join();
}

// #[cgf(test)]
// mod test {
//     use super::*;
//     use crossbeam_channel::unbounded;
// }
