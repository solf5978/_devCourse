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
fn main() {}
