import re


def normalize(text: str) -> str:
    pattern = re.compile(r"\W+")
    return pattern.sub(repl="", string=text).lower()


def cipher_text(text: str) -> str:
    plain_text = normalize(text=text)

    length = len(plain_text)
    rows = int(length**0.5)
    rows = rows + 1 if rows * (rows + 1) < length else rows
    cols = rows + 1 if rows**2 < length else rows

    plain_text += " " * (rows * cols - length)

    if rows <= 1:
        return plain_text

    text_rows = [plain_text[i : cols + i] for i in range(0, len(plain_text), cols)]
    text_cols = []

    for i in range(cols):
        row = "".join(text_rows[j][i] for j in range(rows))
        text_cols.append(row)

    return " ".join(text_cols)
