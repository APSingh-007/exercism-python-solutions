from random import randint

ABILITIES = {
    "strength",
    "dexterity",
    "constitution",
    "intelligence",
    "wisdom",
    "charisma",
}


class Character:
    def __init__(self):
        for ability in ABILITIES:
            setattr(self, ability, self.ability())

        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self) -> int:
        rolls = [randint(1, 6) for _ in range(4)]
        return sum(rolls) - min(rolls)


def modifier(const: int):
    return (const - 10) // 2
