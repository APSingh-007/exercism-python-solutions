from string import ascii_lowercase as alphabets
from random import choice

ORDER: dict = {char: i for i, char in enumerate(alphabets)}


class Cipher:
    def __init__(self, key=None):
        self.key: str = key if key else "".join((choice(alphabets) for _ in range(20)))

    def encode(self, text: str, reverse: bool = False) -> str:
        result = ""
        keys = [ORDER[char] for char in self.key]
        while len(keys) < len(text):
            keys += keys

        for i, char in enumerate(text):
            cipher_char_pos = (
                (ORDER[char] - keys[i]) if reverse else (keys[i] + ORDER[char]) % 26
            )
            result += alphabets[cipher_char_pos]

        return result

    def decode(self, text: str) -> str:
        return self.encode(text=text, reverse=True)
