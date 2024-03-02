use std::rc::Rc;
fn main() {
    let val = 5;
    let val2 = Box::new(2);
    println!("{}", val * *val2);

    let rc_value = String::from("RC Value");

    {
        let rc: Rc<String> = Rc::new(rc_value);
        println!("{}", Rc::strong_count(&rc));
    }
}
