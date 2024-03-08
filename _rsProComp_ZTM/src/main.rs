use std::convert::TryFrom;
use thiserror::Error;

#[derive(Debug, Error)]
enum RgbError {
    #[error("Missing Hash Value For Color")]
    MissingHash,
    #[error("Format Error w Digit: {0}")]
    ParseError(std::num::ParseIntError),
    #[error("Missing Characters")]
    LengthError,
}
#[derive(Debug, Eq, PartialEq)]
struct Rgb(u8, u8, u8);

fn main() {}

#[cfg(test)]
mod test {
    use super::Rgb;
    use std::convert::TryFrom;

    #[test]
    fn converts_valid_hex_color() {
        let expected = Rgb(0, 204, 102);
        let actual = Rgb::try_from("#00cc66");
        assert_eq!(
            actual.is_ok(),
            true,
            "Valid HEX Code Should be converted to Rgb"
        );
        assert_eq!(actual.unwrap(), expected, "Wrong Rgb Value");
    }

    #[test]
    fn fails_on_invalid_hex_digits() {
        assert_eq!(Rgb::try_from("0011yy").is_err(), true, "Invalid Hex Color");
    }
}
