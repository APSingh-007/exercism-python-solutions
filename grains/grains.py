def square(number):
    if number in range(1, 65):
        return 2 ** (number - 1)
    raise ValueError("square must be between 1 and 64")


def total():
    total_grains = 0
    for num in range(1, 65):
        total_grains += square(num)
    return total_grains
