COLORS_VALUES = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}


def value(colors: list) -> int:
    result = 0
    for index, color in enumerate(colors):
        result = result * 10 + COLORS_VALUES[color]
        if index == 1:
            break
    return result
