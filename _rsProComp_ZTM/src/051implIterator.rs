struct ScoreMultiplier {
    amount: usize,
    per_iteration: usize,
    per_iteration_bonus: usize,
}

impl ScoreMultiplier {
    fn new() -> Self {
        Self {
            amount: 0,
            per_iteration: 1,
            per_iteration_bonus: 0,
        }
    }
}

impl Iterator for ScoreMultiplier {
    type Item = usize;
    fn next(&mut self) -> Option<Self::Item> {
        self.amount += self.per_iteration + self.per_iteration_bonus;
        Some(self.amount)
    }
}

fn main() {
    let mut multiplier = ScoreMultiplier::new();
    println!("{:?}", multiplier.next());
    println!("{:?}", multiplier.next());
    println!("{:?}", multiplier.next());

    println!("Per Iteration Bonus = 2");
    multiplier.per_iteration_bonus = 2;
    println!("{:?}", multiplier.next());
    println!("{:?}", multiplier.next());
    println!("{:?}", multiplier.next());
}
