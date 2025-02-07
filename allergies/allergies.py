ALLERGENS = (
    "eggs",
    "peanuts",
    "shellfish",
    "strawberries",
    "tomatoes",
    "chocolate",
    "pollen",
    "cats",
)


class Allergies:
    def __init__(self, score):
        self.allergies = [
            allergen for i, allergen in enumerate(ALLERGENS) if score & 1 << i != 0
        ]

    def allergic_to(self, item):
        return item in self.lst

    @property
    def lst(self) -> list:
        return self.allergies
