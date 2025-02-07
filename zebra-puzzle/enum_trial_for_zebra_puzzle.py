from enum import Flag, auto

NATIONALITY = "Nationality"
COLOUR = "Colour"
PET = "Pet"
DRINK = "Drink"
HOBBY = "Hobby"


class Table:
    # Since there are five houses, we will create a table class with only 5 houses and required properties
    def __init__(self) -> None:
        self.table: dict = {
            NATIONALITY: [None] * 5,
            COLOUR: [None] * 5,
            PET: [None] * 5,
            DRINK: [None] * 5,
            HOBBY: [None] * 5,
        }

    def __repr__(self) -> str:
        sep = "|"
        representation = f"House No.{sep :>4} H0{sep :>11} H1{sep :>11} H2{sep :>11} H3{sep :>11} H4{sep :>11}"
        for key in self.table.keys():
            data = "| ".join(f"{str(item) :<12}" for item in self.table[key])
            representation += "\n" + f"{key :<12}| " + data + sep

        return representation


class Nationality(Flag):
    NORWEGIAN = auto()
    UKRAINIAN = auto()
    ENGLISH = auto()
    SPANIARD = auto()
    JAPANESE = auto()


class Colour(Flag):
    RED = auto()
    GREEN = auto()
    IVORY = auto()
    YELLOW = auto()
    BLUE = auto()


class Pet(Flag):
    HORSE = auto()
    SNAIL = auto()
    DOG = auto()
    ZEBRA = auto()
    FOX = auto()


class Drink(Flag):
    ORANGE_JUICE = auto()
    TEA = auto()
    MILK = auto()
    COFFEE = auto()
    WATER = auto()


class Hobby(Flag):
    DANCING = auto()
    PAINTING = auto()
    READING = auto()
    FOOTBALL = auto()
    CHESS = auto()


"""
The Spaniard owns the dog.
The person in the green house drinks coffee.
The Ukrainian drinks tea.

The snail owner likes to go dancing.
The person in the yellow house is a painter.


The person who enjoys reading lives in the house next to the person with the fox.
The painter's house is next to the house with the horse.
The person who plays football drinks orange juice.
The Japanese person plays chess.

"""


def get_possiblities(table: Table, propertry_1: str, property_2: str) -> int:
    possibilities = 0
    places = []
    for i, item_1 in enumerate(table.table[propertry_1]):
        if possibilities > 2:
            # We shall return 0 if options cross 2 as we will first fill 2 options to reduce computation
            return 0, places
        if item_1 is None:
            for j, item_2 in enumerate(table.table[property_2]):
                if item_2 is None:
                    places.append({propertry_1: i, property_2: j})
                    possibilities += 1
    return possibilities, places


# The Englishman lives in the red house.


# The person in the middle house drinks milk.
def middle_house(table: Table) -> Table:
    # set the middle house (house no. 2 (since numbered 0 to 4)) to drink milk
    table.table[DRINK][2] = Drink.MILK
    return table


# The Norwegian lives in the first house.
def first_house(table: Table) -> Table:
    # set the first house to be of norwegian
    table.table[NATIONALITY][0] = Nationality.NORWEGIAN
    return table


# The Norwegian lives next to the blue house.
def blue_house(table: Table) -> Table:
    # set the house next to norwegian house to be blue
    table.table[COLOUR][1] = Colour.BLUE
    return table


# The green house is immediately to the right of the ivory house.
def green_ivory(table: Table) -> Table:
    pass


def drinks_water():
    pass


def owns_zebra():
    pass


def constraints():
    pass


print(Table())
