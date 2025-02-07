def is_isogram(string: str) -> bool:
    only_alpha = ""
    for ltr in string.lower():
        if ltr.isalpha():
            if ltr in only_alpha:
                return False
            only_alpha += ltr
    return True
