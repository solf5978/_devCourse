struct GroceryItem {
    qty: i32,
    id: i32,
}

fn display_qty(item: &GroceryItem) {
    println!("qty -> {:?}", item.qty);
}

fn display_id(item: &GroceryItem) {
    println!("id -> {:?}", item.id);
}

fn main() {
    let item1 = GroceryItem { qty: 3, id: 100 };
    display_qty(&item1);
    display_id(&item1);
}
