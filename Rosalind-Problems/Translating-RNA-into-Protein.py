def Translating_RNA_into_Protein(RNA):
    protein = []
    i = 0
    while codon_table.get(RNA[i:i+3]) != "Stop":
        protein.append(codon_table.get(RNA[i:i+3]))
        i = i + 3

    protein = ''.join(protein)
    return protein
