def primes(limit):
    numbers = {i: True for i in range(2, limit + 1)}

    for k in numbers.keys():
        if numbers[k]:
            for i in range(k * k, limit + 1, k):
                numbers[i] = False

    return [num for num in numbers.keys() if numbers[num]]
