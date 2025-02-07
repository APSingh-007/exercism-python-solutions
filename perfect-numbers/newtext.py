def classify(number: int) -> str:
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if not number > 0:
        raise ValueError("Classification is only possible for positive integers.")

    results = {0: "perfect", 1: "abundant", -1: "deficient"}
    return results[check(number)]


def check(n):
    factors = set()

    for i in range(1, int(n**0.5) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            factors |= {i, div}

    factors.remove(n)
    diff = sum(factors) - n
    return 0 if diff == 0 else diff / abs(diff)
