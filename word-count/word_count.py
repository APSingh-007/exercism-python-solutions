import re


def count_words(sentence: str) -> str:
    pattern = r"[a-zA-Z\d]+(?:'[a-z]+)?"
    words = re.findall(pattern, sentence.lower())

    return {w: words.count(w) for w in words}
