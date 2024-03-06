trait Body {}

trait Color {}

struct Vehicle<T, U>
where
    T: Body,
    U: Color,
{
    body: T,
    color: U,
}

impl<T: Body, U: Color> Vehicle<T, U> {
    pub fn new(body: T, color: U) -> Self {
        Self { body, color }
    }
}
fn main() {}
