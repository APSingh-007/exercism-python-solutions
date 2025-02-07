fulfillment_cart = {
    "Orange": [1, "Aisle 4", False],
    "Milk": [2, "Aisle 2", True],
    "Banana": [3, "Aisle 5", False],
    "Apple": [2, "Aisle 4", False],
}
store_inventory = {
    "Banana": [15, "Aisle 5", False],
    "Apple": [12, "Aisle 4", False],
    "Orange": [1, "Aisle 4", False],
    "Milk": [4, "Aisle 2", True],
}

for item in store_inventory:
    print(type(store_inventory[item][0]), store_inventory[item][0])
    print(type(fulfillment_cart[item][0]), fulfillment_cart[item][0])
    inventory_remaining = store_inventory[item][0] - fulfillment_cart[item][0]
    print("Inventory Remaining --> ", inventory_remaining)
print(store_inventory)
