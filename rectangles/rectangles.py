def rectangles(strings: list[str]) -> int:
    def find_vertices(string):
        return [
            (r, c)
            for r, line in enumerate(string)
            for c, char in enumerate(line)
            if char == "+"
        ]

    def is_rectangle(top_left, bottom_right):
        r1, c1 = top_left
        r2, c2 = bottom_right
        upper_side = strings[r1][c1 : c2 + 1]
        lower_side = strings[r2][c1 : c2 + 1]
        left_side = [strings[r][c1] for r in range(r1, r2 + 1)]
        right_side = [strings[r][c2] for r in range(r1, r2 + 1)]
        return all(char in "+-" for char in {*upper_side, *lower_side}) and all(
            char in "+|" for char in {*left_side, *right_side}
        )

    vertices = find_vertices(strings)
    counter = 0
    for top_left in vertices:
        for bottom_right in vertices:
            if top_left[0] < bottom_right[0] and top_left[1] < bottom_right[1]:
                if is_rectangle(top_left, bottom_right):
                    counter += 1
    return counter
