def is_armstrong_number(number: int):
    num_to_string = str(number)
    sum_of_powers: int = 0

    for digit in num_to_string:
        sum_of_powers += int(digit) ** len(num_to_string)

    return number == sum_of_powers
