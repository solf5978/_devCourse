fn main() {
    let vec = vec![1, 3, 5, 6, 7];
    let result: Vec<i16> = vec.iter().map(|x| x * 10).collect();
    println!("{:?}", vec);
    println!("{:?}", result);
}
