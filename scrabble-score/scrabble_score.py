POINTS = {
    "AEIOULNRST": 1,
    "DG": 2,
    "BCMP": 3,
    "FHVWY": 4,
    "K": 5,
    "JX": 8,
    "QZ": 10,
}


def score(word: str) -> int:
    score = 0
    for w in word.upper():
        for item in POINTS.keys():
            if w in item:
                score += POINTS[item]
    return score
