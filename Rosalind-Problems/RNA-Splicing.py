def Transcribing_DNA_into_RNA(genome):
    RNA = []
    for l in genome:
        if l == "T":
            RNA.append("U")
        else:
            RNA.append(l)
    RNA = ''.join(RNA)
    return RNA

codon_table = {
    'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
    'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
    'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
    'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
    'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
    'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
    'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
    'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
    'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
    'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
    'UAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
    'UAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
    'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
    'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
    'UGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
    'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
}

def Translating_RNA_into_Protein(RNA):
    protein = []
    i = 0
    while codon_table.get(RNA[i:i+3]) != "M":
        i = i + 1
    while codon_table.get(RNA[i:i+3]) != "Stop":
        protein.append(codon_table.get(RNA[i:i+3]))
        i = i + 3

    protein = ''.join(protein)
    return protein

def function (DNA):

    string = list(DNA.values())[0]
    substrings = list(DNA.values())[1:]

    for substring in substrings:
        if substring in string:
            string = string.replace(substring, '')

    return Translating_RNA_into_Protein((Transcribing_DNA_into_RNA(string)))
