grocery_list = [
    {"item_name" : "Apples", "price": 1.5, "qty": 1,},
    {"item_name" : "Bpples", "price": 12.5, "qty": 2,},
    {"item_name" : "Cpples", "price": 13.5, "qty": 3,},
    {"item_name" : "Dpples", "price": 13.5, "qty": 4,},
    {"item_name" : "Epples", "price": 14.5, "qty": 5,},
    {"item_name" : "Fpples", "price": 15.5, "qty": 6,},
    {"item_name" : "Gpples", "price": 16.5, "qty": 7,},
    {"item_name" : "Hpples", "price": 17.5, "qty": 8,},
]

buget = 35.0
cart = []

def buy_item(item):
    price = item["price"]
    qty = item["qty"]

    global buget

    qty_price = price * qty
    if(buget > qty_price):
        buget -= qty_price
        cart.append(item)

for item in grocery_list:
    buy_item(item)

for item in cart:
    print(f'There are {item["qty"]} p of {item["item_name"]} in the cart')

print(f"remaining buget -> {budget}")