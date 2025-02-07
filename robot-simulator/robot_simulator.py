EAST = (1, 0)
NORTH = (0, 1)
WEST = (-1, 0)
SOUTH = (0, -1)

DIRECTION = (EAST, NORTH, WEST, SOUTH)


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.coordinates = (x_pos, y_pos)
        self.direction = direction

    def move(self, commands=""):
        for c in commands:
            if c == "A":
                self.coordinates = (
                    self.coordinates[0] + self.direction[0],
                    self.coordinates[1] + self.direction[1],
                )
            elif c == "L":
                self.direction = DIRECTION[(DIRECTION.index(self.direction) + 1) % 4]
            else:
                DIR = DIRECTION[::-1]
                self.direction = DIR[(DIR.index(self.direction) + 1) % 4]
