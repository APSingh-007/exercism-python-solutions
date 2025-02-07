HEX_0x80 = 0b10000000

HEX_0x7F = 0b01111111

LIMIT_32_BITS = 2**32 - 1


def encode(numbers: list[int]) -> list[int]:
    result: list[int] = []
    for num in numbers:
        encoded: list[int] = []
        if num < 0 or num > LIMIT_32_BITS:
            raise ValueError(f"{num} not in range (0, {LIMIT_32_BITS})")

        while num:
            snip: int = HEX_0x80 | (num & HEX_0x7F)
            encoded.append(snip)
            num = num >> 7

        if not encoded:
            encoded.append(0)

        encoded[0] = encoded[0] & HEX_0x7F
        result.extend(reversed(encoded))

    return result


def decode(bytes_: list[int]) -> list[int]:
    if bytes_[-1] & HEX_0x80:
        raise ValueError("incomplete sequence")
    result: list[int] = []
    number: int = 0

    for byte_ in bytes_:
        number = (number << 7) | (byte_ & HEX_0x7F)
        if not (byte_ & HEX_0x80):
            result.append(number)
            number = 0

    print([hex(x) for x in result])
    return result
