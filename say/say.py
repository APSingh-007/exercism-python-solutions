ONES = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

TENS = [
    "",
    [
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ],
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]

DENOMINATION = ["", "thousand", "million", "billion"]


def say(number: int) -> str:
    if number > 999_999_999_999 or number < 0:
        raise ValueError("input out of range")
    result = "zero" if number == 0 else ""
    denom = 0

    while number >= 1:
        if number % 1000 < 1:
            number = number // 1000
            denom += 1
            continue
        # Getting digits representing hundreds, tens and ones in a pair of 3 digits
        *_, h, t, o = (int(i) for i in str(1000 + number % 1000))

        hun = ONES[h] + " hundred" if h != 0 else ONES[h]
        ten = TENS[t][o] if t == 1 else TENS[t]
        one = f"-{ONES[o]}" if t > 1 and o > 0 else "" if t != 0 else ONES[o]

        if denom:
            result = f" {DENOMINATION[denom]} {result}"
        space = " " if hun else ""
        result = f"{hun}{space}{ten}{one}{result}"

        number //= 1000
        denom += 1
    return result.strip()
