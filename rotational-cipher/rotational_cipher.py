ALPHBETS = "abcdefghijklmnopqrstuvwxyz"


def rotate(text: str, key: int) -> str:
    cipher = ""
    for ltr in text:
        if ltr.isalpha():
            if ltr.isupper():
                cipher += ALPHBETS[(ALPHBETS.find(ltr.lower()) + key) % 26].upper()
            else:
                cipher += ALPHBETS[(ALPHBETS.find(ltr.lower()) + key) % 26]
        else:
            cipher += ltr
    return cipher
