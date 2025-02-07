def find_anagrams(word: str, candidates: list[str]):
    word = word.casefold()
    anagrams = [
        item
        for item in candidates
        if item.casefold() != word and sorted(item.casefold()) == sorted(word)
    ]
    return anagrams
