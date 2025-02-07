def is_pangram(sentence: str):
    ALPHABETS = set("abcdefghijklmnopqrstuvwxyz")

    return ALPHABETS.issubset(set(sentence.lower()))
