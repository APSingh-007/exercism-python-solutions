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
}
TOLERANCE = {
    "grey": "0.05%",
    "violet": "0.1%",
    "blue": "0.25%",
    "green": "0.5%",
    "brown": "1%",
    "red": "2%",
    "gold": "5%",
    "silver": "10%",
}


def resistor_label(colors: list[str]) -> str:
    base, metric = get_metric(colors)
    tolerance = get_tolerance(colors)

    return f"{base}{metric}{tolerance}"


def get_base(colors: list[str]) -> int:
    base = 0
    base_range = 3 if len(colors) > 4 else 2

    for index in range(base_range):
        try:
            base = base * 10 + BAND_VALUES[colors[index]]
        except Exception:
            print(Exception("only 1 color for base"))
    print(len(str(base)))
    return base


def get_metric(colors: list[str]) -> str:
    base = get_base(colors)
    metric = 0

    try:
        multiplier = colors[3] if len(colors) > 4 else colors[2]
        base = base * (10 ** BAND_VALUES[multiplier])
        print(colors, BAND_VALUES[multiplier], base)
    except Exception:
        print(Exception("multipler not found"))

    while base > 1000:
        base = base / 1000
        metric += 1

    if base > 0 and base % int(base) == 0:
        base = int(base)
    return base, f"{METRIC_PREFIX[metric]}"


def get_tolerance(colors: list[str]) -> str:
    length = len(colors)
    if length < 3:
        return ""
    return f" ±{TOLERANCE[colors[length - 1]]}"
