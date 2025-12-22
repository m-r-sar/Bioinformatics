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

def Transcribing_DNA_into_RNA(genome):
    RNA = {}
    for gen in genome:
        RNA[gen] = ""
        for letter in genome[gen]:
            if letter == "T":
                RNA[gen] += "U"
            else:
                RNA[gen] += letter
    return RNA


def Translating_RNA_into_Protein(RNA):
    protein = {}
    i = 0
    for gen in RNA:
        protein[gen] = ""
        for i in range(0, len(RNA[gen]), 3):
            if not codon_table.get(RNA[gen][i:i+3]) == "Stop":
                protein[gen] += codon_table.get(RNA[gen][i:i+3])
    return protein

def Parse_FASTA(filename):
    result = {}
    string = []
    with open(filename) as file:
        for line in file:
            string.append(line)
    string = ''.join(string)
    string = string.split(">")
    string.remove(string[0])
    for s in string:
        s = s.split('\n')
        s[1] = "".join(s[1:])
        result.update({s[0]: s[1]})
    return result
