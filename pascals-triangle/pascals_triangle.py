def rows(row_count: int) -> list[list[int]]:
    if row_count < 0:
        raise ValueError("number of rows is negative")
    if row_count == 0:
        return []
    if row_count == 1:
        return [[1]]

    result = rows(row_count - 1)

    current_row = [(result[-1][i - 1] + result[-1][i]) for i in range(1, len(result))]

    result.append([1, *current_row, 1])
    return result
