FOOD = ["fly", "spider", "bird", "cat", "dog", "goat", "cow", "horse"]
OBJECTS = FOOD.copy()
OBJECTS[1] = "spider that wriggled and jiggled and tickled inside her"

REACTION = [
    "It wriggled and jiggled and tickled inside her.",
    "How absurd to swallow a bird!",
    "Imagine that, to swallow a cat!",
    "What a hog, to swallow a dog!",
    "Just opened her throat and swallowed a goat!",
    "I don't know how she swallowed a cow!",
]


def recite(start_verse, end_verse):
    poem = []

    for verse in range(start_verse - 1, end_verse):
        start = f"I know an old lady who swallowed a {FOOD[verse]}."
        reaction = [REACTION[verse - 1]] if verse not in (0, 7) else []
        middle = []
        end = (
            "She's dead, of course!"
            if verse == 7
            else "I don't know why she swallowed the fly. Perhaps she'll die."
        )

        if verse != 7:
            for i in range(verse):
                line = f"She swallowed the {FOOD[verse - i]} to catch the {OBJECTS[verse - i - 1]}."
                middle.append(line)

        poem.extend([start, *reaction, *middle, end, ""])

    return poem[:-1]
