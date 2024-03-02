use std::rc::Rc;
fn main() {
    let val = 5;
    let val2 = Box::new(2);
    println!("{}", val * *val2);

    let rc_value = String::from("RC Value");

    {
        let rc: Rc<String> = Rc::new(rc_value);
        println!("{}", Rc::strong_count(&rc));
        {
            let rc2: Rc<String> = Rc::clone(&rc);
            println!("{}", Rc::strong_count(&rc));
            println!("{}", Rc::strong_count(&rc2));
        }
        println!("{}", Rc::strong_count(&rc));
    }
}
