from string import ascii_lowercase as alpha
from math import gcd

M = 26  # Since we are taking 0 to 25 as numbers for the roman letters


def check_GCD(a: int) -> None:
    if gcd(a, M) != 1:
        raise ValueError("a and m must be coprime.")


def encode(plain_text: str, a: int, b: int) -> str:
    # Check whether a and M are co-primes, and raise ValueError if not
    check_GCD(a)
    cipher: str = ""
    counter = 0

    for ltr in plain_text.lower():
        if ltr.isnumeric():
            counter += 1
            cipher += ltr

        if ltr.isalpha():
            # Using E(ltr) = y = (ai - b) % M
            counter += 1
            i = alpha.index(ltr)
            E = (a * i + b) % M
            cipher += alpha[E]

        if counter == 5:
            counter = 0
            cipher += " "

    return cipher.rstrip()


def decode(ciphered_text: str, a: int, b: int) -> str:
    check_GCD(a)

    # using -1 in exp of the pow(base = a, exp = -1, modu = m) function gives modilar inverse of (a mod m)
    mmi = pow(a, -1, M)
    plaintext = ""
    for ltr in ciphered_text.lower():
        # Using D(ltr) = x = mmi * (y - b) % M
        if ltr.isnumeric() or ltr == " ":
            plaintext += ltr if ltr.isnumeric() else ""
            continue
        y = alpha.index(ltr)
        D = (mmi * (y - b)) % M
        plaintext += alpha[D]

    return plaintext
