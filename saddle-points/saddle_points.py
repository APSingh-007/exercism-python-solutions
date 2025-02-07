def saddle_points(matrix: list) -> list:
    breadth = len(matrix)

    res = []
    try:
        for r, row in enumerate(matrix):
            for c, h in enumerate(row):
                column = [matrix[i][c] for i in range(breadth)]
                if min(column) == h == max(row):
                    res.append({"row": r + 1, "column": c + 1})
    except IndexError:
        raise ValueError("irregular matrix")

    return res
