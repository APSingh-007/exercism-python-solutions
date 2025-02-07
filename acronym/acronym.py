def abbreviate(words: str) -> str:
    items = words.replace(".", " ").replace("_", " ").replace("-", " ").upper().split()
    return "".join(ltr[0] for ltr in items)
