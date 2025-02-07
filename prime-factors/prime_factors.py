def gpt_factors(value: int) -> list:
    primes = []
    divisor = 2
    max = int(value**0.5) + 1
    while divisor <= max:
        while value % divisor == 0:
            primes.append(divisor)
            value //= divisor
            max = int(value**0.5) + 1
        divisor += 1 if divisor == 2 else 2
    if value > 2:
        primes.append(value)
    return primes


def factors(value, k=2, lst=None):
    if lst is None:
        lst = []
    while value != 1:
        if value % k == 0:
            lst.append(k)
            value //= k
        else:
            k += 1
    return lst
