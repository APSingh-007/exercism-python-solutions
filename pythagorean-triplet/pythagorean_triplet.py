def triplets_with_sum(number):
    def calculate_medium(small):
        answer: float = (number**2 - 2 * number * small) / (2 * (number - small))
        return int(answer) if answer.is_integer() else 0

    two_sides = (
        (medium, small)
        for small in range(3, number // 3)
        if small < (medium := calculate_medium(small))
    )

    return [
        [small, medium, (medium**2 + small**2) ** 0.5] for medium, small in two_sides
    ]
