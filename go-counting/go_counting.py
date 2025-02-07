WHITE = "W"
BLACK = "B"
NONE = " "
DIRECTION = [(1, 0), (0, -1), (-1, 0), (0, 1)]


class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board: list[str]) -> None:
        if not board or not board[0]:
            raise ValueError("Board does not Exist.")
        self.board = board

    def territory(self, x: int, y: int) -> tuple[str, set]:
        """Find the owner and the territories given a coordinate on
           the board

        Args:
            x (int): Column on the board
            y (int): Row on the board

        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
        """

        y_range = range(len(self.board))
        x_range = range(len(self.board[0]))

        if x not in x_range or y not in y_range:
            raise ValueError("Invalid coordinate")
        if self.board[y][x] != NONE:
            return NONE, set()

        stack = [(x, y)]
        visited = []
        stones = []
        territory = []

        def neighbours(xx: int, yy: int) -> list[tuple[int]]:
            result = []
            for dx, dy in DIRECTION:
                dx, dy = xx + dx, yy + dy
                if (dx, dy) not in visited and dx in x_range and dy in y_range:
                    result.append((dx, dy))

            return result

        while stack:
            current = stack.pop()
            visited.append(current)
            xx, yy = current

            if self.board[yy][xx] == NONE:
                territory.append(current)
                stack.extend(neighbours(xx, yy))
            else:
                stones.append(self.board[yy][xx])

        if len(set(stones)) == 1:
            return stones[0], set(territory)
        return NONE, set(territory)

    def territories(self) -> dict[str, set]:
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        result: dict[str] = {WHITE: set(), BLACK: set(), NONE: set()}
        checked = set()
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                if self.board[y][x] == NONE and (x, y) not in checked:
                    rock, territories = self.territory(x, y)
                    checked |= territories
                    result[rock] |= territories
        return result
