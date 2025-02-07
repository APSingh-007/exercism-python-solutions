NUMBERS = (
    "No green bottles",
    "One green bottle",
    "Two green bottles",
    "Three green bottles",
    "Four green bottles",
    "Five green bottles",
    "Six green bottles",
    "Seven green bottles",
    "Eight green bottles",
    "Nine green bottles",
    "Ten green bottles",
)


def recite(start: int, take: int = 1) -> str:
    res = []
    while take > 0:
        res += [
            f"{NUMBERS[start]} hanging on the wall,",
            f"{NUMBERS[start]} hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            f"There'll be {NUMBERS[start-1].lower()} hanging on the wall.",
            "",
        ]
        start -= 1
        take -= 1
    return res[:-1]
