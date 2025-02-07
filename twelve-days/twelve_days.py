VERSES = [
    "a Partridge in a Pear Tree.",
    "two Turtle Doves, ",
    "three French Hens, ",
    "four Calling Birds, ",
    "five Gold Rings, ",
    "six Geese-a-Laying, ",
    "seven Swans-a-Swimming, ",
    "eight Maids-a-Milking, ",
    "nine Ladies Dancing, ",
    "ten Lords-a-Leaping, ",
    "eleven Pipers Piping, ",
    "twelve Drummers Drumming, ",
]
DAYS = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
]


def recite(start_verse, end_verse):
    result = []
    for verse in range(start_verse, end_verse + 1):
        starter = f"On the {DAYS[verse - 1]} day of Christmas my true love gave to me: "
        mid_part = "".join(VERSES[i - 2] for i in range(verse + 1, 2, -1))

        joiner = "and " if mid_part else ""
        result.append(f"{starter}{mid_part}{joiner}{VERSES[0]}")
    return result
