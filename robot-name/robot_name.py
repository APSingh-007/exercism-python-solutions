from string import ascii_uppercase, digits
from random import choices as choose, seed

cache = set()


class Robot:
    def __init__(self):
        self.name = self.rename()

    def rename(self):
        seed()
        return "".join(choose(ascii_uppercase, k=2) + choose(digits, k=3))

    def reset(self):
        while True:
            name = self.rename()
            if name not in cache:
                self.name = name
                cache.add(name)
                break
