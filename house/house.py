NOUNS = [
    "house that Jack built",
    "malt",
    "rat",
    "cat",
    "dog",
    "cow with the crumpled horn",
    "maiden all forlorn",
    "man all tattered and torn",
    "priest all shaven and shorn",
    "rooster that crowed in the morn",
    "farmer sowing his corn",
    "horse and the hound and the horn",
]

VERBS = [
    "lay in",
    "ate",
    "killed",
    "worried",
    "tossed",
    "milked",
    "kissed",
    "married",
    "woke",
    "kept",
    "belonged to",
    "",
]


def recite(start_verse: int, end_verse: int) -> list:
    return [create_rhyme(index) for index in range(start_verse - 1, end_verse)]


def create_rhyme(rhyme_no: int) -> str:
    rhyme = "This is the "

    while rhyme_no > 0:
        rhyme = rhyme + f"{NOUNS[rhyme_no]} that {VERBS[rhyme_no - 1]} the "
        rhyme_no -= 1

    return rhyme + f"{NOUNS[0]}."
