vowels = ("a", "e", "i", "o", "u")
cond_vowel = ("xr", "yt")


def translate(text: str) -> str:
    result = ""
    for word in text.casefold().split(" "):
        leading = ""
        for i, ltr in enumerate(word):
            tail = word[i:]
            if tail.startswith(vowels) or (i != 0 and ltr == "y"):
                result += tail + leading + "ay "
                break
            if i == 0 and tail.startswith(cond_vowel):
                result += tail + "ay "
                break
            if tail.startswith("qu"):
                result += tail[2:] + leading + "quay "
                break
            leading += ltr
    return result.strip(" ")
