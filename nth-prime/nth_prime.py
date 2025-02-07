def prime(number: int) -> int:
    if number < 1:
        raise ValueError("there is no zeroth prime")

    primes = [2]
    num = 3
    while len(primes) < number:
        is_prime = True
        sqrt = num**0.5
        for div in primes:
            if num % div == 0:
                is_prime = False
                break
            if div > sqrt:
                break
        if is_prime:
            primes.append(num)
        num += 2

    return primes[number - 1]
