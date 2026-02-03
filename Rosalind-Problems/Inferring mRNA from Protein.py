codon_counts = {
    "F": 2,
    "L": 6,
    "I": 3,
    "V": 4,
    "M": 1,
    "S": 6,
    "P": 4,
    "T": 4,
    "A": 4,
    "Y": 2,
    "H": 2,
    "N": 2,
    "D": 2,
    "Q": 2,
    "K": 2,
    "E": 2,
    "C": 2,
    "R": 6,
    "G": 4,
    "W": 1
}

def Inferring_mRNA_from_Protein(protein):
    total = 1
    for acid in protein:
        total *= codon_counts[acid]

    total *= 3 # for 3 Stop codons
    return total % 1000000
