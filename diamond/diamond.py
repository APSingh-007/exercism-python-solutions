def rows(letter: str) -> list:
    ascii_A = ord("A")
    len = ord(letter) - ascii_A
    result = []
    for i in range(0, len + 1):
        spacers = " " * (len - i)
        mid = (" " * (i * 2 - 1)).join(chr(ascii_A + i) * (1 if i == 0 else 2))
        result.append(f"{spacers}{mid}{spacers}")
    return result + result[::-1][1:]
