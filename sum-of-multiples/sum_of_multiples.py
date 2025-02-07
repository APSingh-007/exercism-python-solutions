def sum_of_multiples(limit, numbers):
    return sum({i for num in numbers if num > 0 for i in range(num, limit, num)})
