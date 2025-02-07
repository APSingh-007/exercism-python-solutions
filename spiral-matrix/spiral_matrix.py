direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def spiral_matrix(size: int) -> list[list[int]]:
    result = [[0 for _ in range(size)] for _ in range(size)]

    dir = 0
    step: int = size
    count: int = 1
    x, y = 0, -1
    num = 1

    for run in range(size * 2 - 1):
        for _ in range(step):
            x += direction[dir][0]
            y += direction[dir][1]
            result[x][y] = num
            num += 1
        count += 1
        if count == 2:
            count = 0
            step -= 1

        dir = (dir + 1) % 4
    return result
