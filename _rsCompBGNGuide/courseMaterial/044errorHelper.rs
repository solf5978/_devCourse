use std::fs::File;

#[allow(unused_variables)]
#[allow(unused_assignments)]

fn main() {
    // let f = File::open("main.jpg").unwrap();
    let f = File::open("main.jpg").expect("Unable to open file");
}