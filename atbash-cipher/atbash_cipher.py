import string

TRANS = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[::-1])


def encode(plain_text: str, encode=True) -> str:
    cipher = "".join(char for char in plain_text.lower() if char.isalnum()).translate(
        TRANS
    )
    cipher = (
        " ".join(cipher[i : i + 5] for i in range(0, len(cipher), 5))
        if encode
        else cipher
    )

    return cipher


def decode(ciphered_text: str) -> str:
    return encode(ciphered_text, False)
