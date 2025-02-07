from typing import Optional

DIRECTIONS = (
    (1, 0),  # left to right
    (0, 1),  # top to bot
    (1, 1),  # top-left to bot-right
    (-1, 1),  # top-right to bot-left
)


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"point(x: {self.x}, y: {self.y})"

    def __eq__(self, other: object) -> bool:
        return self.x == other.x and self.y == other.y


class WordSearch:
    def __init__(self, puzzle: list[str]) -> None:
        if not puzzle:
            raise ValueError("Puzzle Box is Empty")
        self.puzzle = puzzle.copy()
        self.height = len(puzzle)
        self.width = len(puzzle[0])

    def search(self, word: str) -> Optional[tuple[Point, Point]]:
        # Check each point in all 8 direction (4 in DIRECTIONS and 4 in respective opposite directions)
        for x in range(self.width):
            for y in range(self.height):
                if points := self.check_word(word, x, y):
                    return points

    def check_word(self, word: str, x: int, y: int) -> Optional[tuple[Point, Point]]:
        wlen = len(word)

        for x_dir, y_dir in DIRECTIONS:
            # Calculate the end points for a string block with same length as the word in given direction
            x_end = x + x_dir * (wlen - 1)
            y_end = y + y_dir * (wlen - 1)

            # Check if end points lie outside of puzzle box, if yes, continue for next direction
            if not (0 <= x_end < self.width) or not (0 <= y_end < self.height):
                continue

            # Get the string block with same length as given word in the current direction
            # Once we have the required string we can reverse it to check if it matches the word in opposite direction
            to_check = "".join(
                self.puzzle[y + y_dir * i][x + x_dir * i] for i in range(wlen)
            )
            # Check in current direction
            if word == to_check:
                return Point(x, y), Point(x_end, y_end)
            # Check in opposite direction
            if word == to_check[::-1]:
                return Point(x_end, y_end), Point(x, y)

        return None
