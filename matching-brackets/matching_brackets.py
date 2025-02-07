bracs = {"[": "]", "{": "}", "(": ")"}


def is_paired(input_string: str) -> bool:
    stack = []
    for char in input_string:
        if char in bracs.keys():
            stack.append(char)
        if char in bracs.values():
            if not stack or bracs[stack.pop()] != char:
                return False
    return not stack
