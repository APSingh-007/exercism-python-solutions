ROMAN = {
    0: ["M"],
    1: ["C", "D", "M"],
    2: ["X", "L", "C"],
    3: ["I", "V", "X"],
}


def roman(number: int) -> str:
    if number > 3999 or number < 1:
        raise ValueError("Invalid Number")

    res = ""

    nums = [int(i) for i in "0" * (4 - len(str(number))) + str(number)]

    print(nums)
    for i, n in enumerate(nums):
        if n == 0:
            continue
        if n <= 3:
            res += f"{ROMAN[i][0] * n}"
        else:
            pref = ROMAN[i][0] if n in (4, 9) else ""
            post = ROMAN[i][0] * (n - 5) if n in (6, 7, 8) else ""
            mid = ROMAN[i][2] if n == 9 else ROMAN[i][1]
            res += f"{pref}{mid}{post}"

    return res
