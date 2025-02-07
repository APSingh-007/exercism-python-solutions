directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]


def annotate(minefield: list) -> list:
    # Function body starts here

    length = len(minefield)
    if minefield:
        width: int = len(minefield[0])
        for row in minefield:
            if len(row) != width:
                raise ValueError("The board is invalid with current input.")

    for y in range(length):
        result = ""
        for x in range(width):
            if minefield[y][x] == " ":
                result += count_mines(length, width, minefield, y, x)
            elif minefield[y][x] == "*":
                result += "*"
            else:
                raise ValueError("The board is invalid with current input.")

        minefield[y] = result

    print(minefield)
    return minefield


def count_mines(length: int, width: int, minefield: list, y, x) -> str:
    mines = 0
    for dx, dy in directions:
        if (
            0 <= x + dx < width
            and 0 <= y + dy < length
            and minefield[y + dy][x + dx] == "*"
        ):
            mines += 1
    return str(mines) if mines else " "
