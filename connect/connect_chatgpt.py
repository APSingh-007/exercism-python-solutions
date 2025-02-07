"""
x       left --> right

"""


class ConnectGame:
    def __init__(self, board):
        self.board = [line.strip().split() for line in board.strip().split("\n")]
        self.height = len(self.board)
        self.width = len(self.board[0]) if self.height > 0 else 0

    def get_winner(self):
        if self.check_winner("O"):
            return "O"
        elif self.check_winner("X"):
            return "X"
        else:
            return ""

    def check_winner(self, player):
        visited = set()
        if player == "O":
            for x in range(self.width):
                if self.board[0][x] == player:
                    if self.dfs(x, 0, player, visited):
                        return True
        elif player == "X":
            for y in range(self.height):
                if self.board[y][0] == player:
                    if self.dfs(0, y, player, visited):
                        return True
        return False

    def dfs(self, x, y, player, visited):
        if player == "O" and y == self.height - 1:
            return True
        if player == "X" and x == self.width - 1:
            return True

        visited.add((x, y))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, -1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < self.width
                and 0 <= ny < self.height
                and (nx, ny) not in visited
                and self.board[ny][nx] == player
            ):
                if self.dfs(nx, ny, player, visited):
                    return True

        return False
