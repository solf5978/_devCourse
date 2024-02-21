fn main() {
    const MEANING_OF_LIFE: u8 = 42;
    static mut HELLO_WORLD: u8 = 0x25;
    // MUST GIVEN TYPE
    println!("{}", MEANING_OF_LIFE);
    unsafe {
        println!("{}", HELLO_WORLD);
    }
}
