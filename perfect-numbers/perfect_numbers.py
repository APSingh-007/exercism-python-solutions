def classify(number):
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    aliquot_sum = (
        sum(
            i + number // i if i != number // i else i
            for i in range(1, int(number**0.5) + 1)
            if number % i == 0
        )
        - number
    )
    if aliquot_sum < number:
        return "deficient"
    if aliquot_sum > number:
        return "abundant"
    return "perfect"
