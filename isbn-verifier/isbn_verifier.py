def is_valid(isbn: str) -> bool:
    sum = 0
    exp = 10

    for digit in isbn:
        if digit.isalnum():
            if digit == "X" and exp == 1:
                sum += 10
            elif digit.isdigit():
                sum += int(digit) * exp
            else:
                return False
            exp -= 1

    return sum % 11 == 0 and exp == 0
