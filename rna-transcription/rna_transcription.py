TRANS_TABLE = str.maketrans("GCTA", "CGAU")


def to_rna(dna_strand: str) -> str:
    return dna_strand.translate(TRANS_TABLE)
