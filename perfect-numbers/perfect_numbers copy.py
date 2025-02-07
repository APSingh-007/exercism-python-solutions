def classify(number: int) -> str:
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if not number > 0:
        raise ValueError("Classification is only possible for positive integers.")

    results = {0: "perfect", 1: "abundant", -1: "deficient"}
    return results[perfect(number)]


def perfect(number) -> int:
    sum = 0
    for factor in range(1, number // 2 + 1):
        if number % factor == 0:
            sum += factor
    diff = sum - number

    return 0 if diff == 0 else diff / abs(diff)
