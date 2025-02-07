def maximum_value(maximum_weight: int, items: list[dict[str:int]]) -> int:
    # DP table with dimensions (number of items + 1) x (maximum_weight + 1)
    table = [[0] * (maximum_weight + 1) for _ in range(len(items) + 1)]

    # Loop through each item (index starts from 1 because table[0] is for no items)
    for last_row, item in enumerate(items):
        for current_col in range(1, maximum_weight + 1):
            # here, current_col also equals to max weight of the given cell
            if current_col < item["weight"]:
                # If the item cannot fit in the current weight capacity, use value from previous row for same max_weight
                value = table[last_row][current_col]
            else:
                # Max value between not taking and taking the item
                value = max(
                    table[last_row][current_col],  # skipping current item
                    item["value"] + table[last_row][current_col - item["weight"]],
                    # taking current item and using max value for remaining weight
                )
            table[last_row + 1][current_col] = value

    # the last cell of table has maxx value
    return table[-1][-1]
