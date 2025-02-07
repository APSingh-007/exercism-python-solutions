def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    if input_base == output_base:
        return digits

    number = 0
    result = []
    # Convert to base10
    for i, dig in enumerate(reversed(digits)):
        if 0 <= dig < input_base:
            number += dig * (input_base**i)
        else:
            raise ValueError("all digits must satisfy 0 <= d < input base")
    # Convert to output_base
    while number:
        number, mod = divmod(number, output_base)
        result.insert(0, mod)

    return result or [0]
