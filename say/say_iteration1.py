ONES = {
    "0": "",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}
TWENTIES = {
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen",
}
TENS = {
    "2": "twenty",
    "3": "thirty",
    "4": "forty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety",
}
POSTFIX = ["", "thousand", "million", "billion"]


def say(number: int) -> str:
    if 0 > number or number > 999_999_999_999:
        raise ValueError("input out of range")

    result = "" if number != 0 else "zero"
    three_zeroes = 0
    while number >= 1:
        if number % 1000 < 1:
            number = number // 1000
            three_zeroes += 1
            continue

        h, t, o = "0" * (3 - len(str(number % 1000))) + str(number % 1000)

        h = "" if h == "0" else f"{ONES[h]} hundred"
        if t == "1":
            t = TWENTIES[t + o]
            o = ""
        else:
            t = "" if t == "0" else f"{TENS[t]}"
            o = ONES[o] if t == "" or o == "0" else f"-{ONES[o]}"

        if three_zeroes:
            result = f" {POSTFIX[three_zeroes]} {result}"
        result = f"{h} {t+o}{result}" if h else f"{t+o}{result}"

        three_zeroes += 1
        number = number // 1000

    return result.strip()


print(say(1))
