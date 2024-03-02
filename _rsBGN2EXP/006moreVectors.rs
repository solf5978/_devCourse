// -------------------------------------------------
// 			- Vectors
// -------------------------------------------------

fn main() {
    let mut number_vec: Vec<i32> = vec![4, 5, 6, 8, 9, 10, 11, 12, 15, 16, 12, 10];

    println!("{}", number_vec[0]);
    println!("{:?}", number_vec);

    number_vec[4] = 5;
    println!("{:?}", number_vec);

    let array_with_same_elements: Vec<i32> = vec![0; 10];

    let mut string_array_1 = vec!["apple", "tomato", "grapes"];
    let string_array_2 = vec!["Unknown"; 6];
    string_array_1[0] = "kamran azam";

    let char_array: Vec<char> = vec!['a', 'p', 'p', 'l', 'e'];

    let subset_vec = &number_vec[0..3];
    println!("The subset of values of the array are {:?}", subset_vec);

    println!("Elements in the array are {}", number_vec.len());

    let check_index = number_vec.get(100);
    println!("{:?}", check_index);

    number_vec.push(30);
    number_vec.push(40);
    println!("The values are {:?}", number_vec);

    number_vec.remove(5);
    println!(
        "The array after removing the element at index 5 {:?}",
        number_vec
    );

    println!(
        "The value of 10 exist in the array {}",
        number_vec.contains(&10)
    );
}
