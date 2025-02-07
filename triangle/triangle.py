def no_of_sides(sides: list) -> int:
    """
    0 -> not triangle
    1 -> equilateral / also Isosceles
    2 -> Isosceles
    3 -> Scalene
    """

    unique_sides = set(sides)
    sides.sort()

    if 0 in unique_sides or sum(sides[0:2]) <= sides[2]:
        return 0
    return len(unique_sides)


def equilateral(sides):
    return no_of_sides(sides) == 1


def isosceles(sides):
    return no_of_sides(sides) == 2 or no_of_sides(sides) == 1


def scalene(sides):
    return no_of_sides(sides) == 3
