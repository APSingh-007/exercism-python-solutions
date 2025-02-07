inventory = {"coal": 3, "diamond": 1, "iron": 5}
items = ["diamond", "coal", "iron", "iron"]

for item in items:
    inventory[item] = inventory[item] = (
        0 if inventory[item] == 0 else inventory[item] - 1
    )
print(inventory)
