#[derive(Clone, Copy)]
struct LuggageID(usize);
struct Luggage(LuggageID);
struct CheckIn(LuggageID);
struct OnLoading(LuggageID);
struct OffLoading(LuggageID);
struct AwiatingPickUp(LuggageID);
struct EndCustody(LuggageID);

impl Luggage {
    fn new(id: LuggageID) -> Self {
        Luggage(id)
    }
    fn check_in(self) -> CheckIn {
        CheckIn(self.0)
    }
}

impl CheckIn {
    fn onload(self) -> OnLoading {
        OnLoading(self.0)
    }
}

impl OnLoading {
    fn offload(self) -> OffLoading {
        OffLoading(self.0)
    }
}
impl OffLoading {
    fn carousel(self) -> AwiatingPickUp {
        AwiatingPickUp(self.0)
    }
}

impl AwiatingPickUp {
    fn pick_up(self) -> (Luggage, EndCustody) {
        (Luggage(self.0), EndCustody(self.0))
    }
}
fn main() {
    let id = LuggageID(1);
    let luggage = Luggage::new(id);
    let luggage = luggage.check_in().onload().offload().carousel();
    let (luggage, _) = luggage.pick_up();
}
