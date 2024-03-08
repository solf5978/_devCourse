pub fn trim(msg: &str) -> &str {
    msg.trim()
}

pub fn capitalize(msg: &str) {
    if let Some(letter) = msg.get(0..1) {
        println!("{}{}", letter.to_uppercase(), &msg[1..msg.len()])
    } else {
        println!("{}", msg)
    }
}

pub fn exciting(msg: &str) -> String {
    format!("{}!", msg)
}
