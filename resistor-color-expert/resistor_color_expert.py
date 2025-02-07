COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]

METRIC = [
    " ohms",
    " kiloohms",
    " megaohms",
]

TOLERANCE = {
    "": "",
    "grey": " ±0.05%",
    "violet": " ±0.1%",
    "blue": " ±0.25%",
    "green": " ±0.5%",
    "brown": " ±1%",
    "red": " ±2%",
    "gold": " ±5%",
    "silver": " ±10%",
}


def resistor_label(colors: list[str]) -> str:
    resistance = 0
    metric = 0

    if len(colors) > 3:
        *base, multiplier, tolerance = colors
    else:
        base, multiplier, tolerance = colors, "black", ""

    for item in base:
        resistance = resistance * 10 + COLORS.index(item)
    resistance *= 10 ** COLORS.index(multiplier)

    while resistance > 1000:
        resistance /= 1000
        metric += 1
    if resistance > 0 and resistance % int(resistance) == 0:
        resistance = int(resistance)

    return f"{resistance}{METRIC[metric]}{TOLERANCE[tolerance]}"
