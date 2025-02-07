def encode(message: str, rails: int) -> str:
    if rails == 1:
        return message

    fence_map = zig_zag(len(message), rails)
    result = ""

    for line in range(rails):
        for pos in fence_map[line]:
            result += message[pos]

    return result


def decode(encoded_message: str, rails: int) -> str:
    if rails == 1:
        return encoded_message

    fence_map = zig_zag(len(encoded_message), rails)
    result = [""] * len(encoded_message)
    counter = 0

    for line in range(rails):
        for pos in fence_map[line]:
            result[pos] = encoded_message[counter]
            counter += 1

    return "".join(result)


def zig_zag(length: int, rails: int) -> list[int]:
    line = 0
    fence = [[] for _ in range(rails)]
    direction = -1

    for pos in range(length):
        fence[line].append(pos)

        if line in (0, rails - 1):
            direction *= -1
        line += direction

    return fence
