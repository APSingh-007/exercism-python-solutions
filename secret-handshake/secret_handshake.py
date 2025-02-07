COMMANDS = ["wink", "double blink", "close your eyes", "jump"]


def commands(binary_str: str) -> str:
    if 1 < int(binary_str, 2) > 31:
        raise ValueError("Only binary values between 1 and 31 are accepted")

    result = []
    binary_str = binary_str[::-1]

    for index, item in enumerate(binary_str):
        if index == 4 and item == "1":
            result = result[::-1]
            break
        if item == "1":
            result.append(COMMANDS[index])

    return result
