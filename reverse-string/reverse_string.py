def reverse(text: str):
    rev = ""
    for i in text.strip():
        rev = i + rev
    return rev
