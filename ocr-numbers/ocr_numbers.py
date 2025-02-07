NUMBERS = {
    " _ | ||_|   ": "0",
    "     |  |   ": "1",
    " _  _||_    ": "2",
    " _  _| _|   ": "3",
    "   |_|  |   ": "4",
    " _ |_  _|   ": "5",
    " _ |_ |_|   ": "6",
    " _   |  |   ": "7",
    " _ |_||_|   ": "8",
    " _ |_| _|   ": "9",
}


def convert(input_grid: list[str]) -> int:
    total_lines = len(input_grid)
    if total_lines % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if len(input_grid[0]) % 3 != 0:
        raise ValueError("Number of input columns is not a multiple of three")

    result = []

    for top_line in range(0, total_lines, 4):
        res = ""
        for num_start in range(0, len(input_grid[0]), 3):
            ocr = ""
            for line in range(top_line, top_line + 4):
                ocr += input_grid[line][num_start : num_start + 3]

            res += NUMBERS.get(ocr, "?")

        result.append(res)

    return ",".join(result)
