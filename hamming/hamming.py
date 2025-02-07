def distance(strand_a: str, strand_b: str) -> int:
    hamming = 0

    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    for index, genome_a in enumerate(strand_a):
        if strand_b[index] != genome_a:
            hamming += 1
    return hamming
