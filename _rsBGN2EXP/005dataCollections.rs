// -------------------------------------------------
// 			- Tuples
//			- Arrays
// -------------------------------------------------

fn main() {
    let nested_tuple = (4, 5.0, (3, 2), "Hello");
    let element = nested_tuple.2 .0; // or (nested_tuple.2).0, in some earlier version the syntax will be (nested_tuple.2).0
    println!("The value of element is {}", element);

    let empty_tuple = ();

    let mut number_array: [i32; 5] = [4, 5, 6, 8, 9];

    println!("{}", number_array[0]);

    println!("{:?}", number_array);

    number_array[4] = 5;
    println!("{:?}", number_array);

    let array_with_same_elements = [0; 10];

    let mut string_array_1 = ["apple", "tomato", "grapes"];
    let string_array_2 = ["Unknown"; 6];
    string_array_1[0] = "kamran azam";

    let char_array = ['a', 'p', 'p', 'l', 'e'];

    let mut number_array_1: [i32; 5] = [4, 5, 6, 8, 9];

    let subset_array = &number_array_1[0..=3];
    println!("The subset of values of the array are {:?}", subset_array);

    //subset_array[0] = 15;

    println!("Elements in the array are {}", number_array_1.len());

    println!(
        "The array is occupying {} bytes",
        std::mem::size_of_val(&number_array_1)
    );

    // number_array_1[10] = 5;

    let check_index = number_array_1.get(100);
    println!("{:?}", check_index);
}
