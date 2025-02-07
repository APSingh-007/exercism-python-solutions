class Queen:
    def __init__(self, row, column):
        if row < 0:
            raise ValueError("row not positive")
        if row > 7:
            raise ValueError("row not on board")
        if column < 0:
            raise ValueError("column not positive")
        if column > 7:
            raise ValueError("column not on board")

        self.row = row
        self.col = column
        self.attack_points = self.attacks(row, column)

    def can_attack(self, another_queen):
        if (another_queen.row, another_queen.col) == (self.row, self.col):
            raise ValueError("Invalid queen position: both queens in the same square")
        return (another_queen.row, another_queen.col) in self.attack_points

    def attacks(self, row, col):
        d1 = []
        d2 = []

        x = 1
        while row - x >= 0 and col - x >= 0:
            d1.append((row - x, col - x))
            x += 1
        x = 1
        while row + x <= 7 and col + x <= 7:
            d1.append((row + x, col + x))
            x += 1
        x = 1
        while row - x >= 0 and col + x <= 7:
            d2.append((row - x, col + x))
            x += 1
        x = 1
        while row + x <= 7 and col - x >= 0:
            d2.append((row + x, col - x))
            x += 1

        c = [(i, col) for i in range(8) if i != row]
        r = [(row, i) for i in range(8) if i != col]

        return [*d1, *d2, *c, *r]
