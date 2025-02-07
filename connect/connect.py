direction = [(1, 0), (0, -1), (-1, 1), (-1, 0), (0, 1), (1, -1)]


class ConnectGame:
    def __init__(self, board):
        self.board = [line.strip().split() for line in board.strip().split("\n")]
        self.height = len(self.board)
        self.width = len(self.board[0]) if self.height else 0

    def get_winner(self) -> str:
        for x in range(self.width):
            if self.board[0][x] == "O":
                if self.dfs_check(x, 0, self.height - 1, "O"):
                    return "O"
        for y in range(self.height):
            if self.board[y][0] == "X":
                if self.dfs_check(0, y, self.width - 1, "X"):
                    return "X"
        return ""

    def dfs_check(self, x: int, y: int, edge: int, player: str) -> bool:
        stack: list = [(x, y)]
        visited: list = []

        if (player == "O" and self.height == 1) or (player == "X" and self.width == 1):
            return True

        while stack:
            x, y = stack[-1]
            visited.append(stack.pop())

            for dx, dy in direction:
                xx, yy = x + dx, y + dy
                if (
                    0 <= xx < self.width
                    and 0 <= yy < self.height
                    and (xx, yy) not in visited
                ):
                    mvn: int = xx if player == "X" else yy

                    if self.board[yy][xx] == player:
                        if mvn == edge:
                            return True
                        stack.append((xx, yy))
        return False
