BAND_VALUES = {
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
METRIC_PREFIX = {
    0: " ohms",
    1: " kiloohms",
    2: " megaohms",
    3: " gigaohms",
    4: " teraohms",
    5: " petaohms",
}


def label(colors: list) -> int:
    base = BAND_VALUES[colors[0]] * 10 + BAND_VALUES[colors[1]]
    no_of_zeros = BAND_VALUES[colors[2]]

    while base > 0 and base % 10 == 0:
        no_of_zeros += 1
        base //= 10
    div, mod = divmod(no_of_zeros, 3)
    resistance = str(base * (10**mod)) + METRIC_PREFIX[div]

    return resistance
