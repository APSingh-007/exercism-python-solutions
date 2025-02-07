MAPPING = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": False,
    "UAG": False,
    "UGA": False,
}


def proteins(strand: str) -> list:
    length = len(strand)
    if length % 3 != 0:
        raise ValueError("Incorrect RNA sequence")
    result = []

    for i in range(0, length, 3):
        condon = strand[i : i + 3]
        if not MAPPING[condon]:
            break
        result.append(MAPPING[condon])

    return result
