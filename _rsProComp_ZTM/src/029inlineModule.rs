mod msg {
    fn trim(msg: &str) -> &str {
        msg.trim()
    }
}

mod math {
    pub fn test1() {}
    pub fn test2() {}
}

fn main() {
    // let result = test1();
    use math::{test1, test2};
    let result = math::test1();
}
