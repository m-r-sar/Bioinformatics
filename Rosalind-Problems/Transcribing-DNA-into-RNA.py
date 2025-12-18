def Transcribing_DNA_into_RNA(genome):
    RNA = []
    for l in genome:
        if l == "T":
            RNA.append("U")
        else:
            RNA.append(l)
    RNA = ''.join(RNA)
    return RNA
