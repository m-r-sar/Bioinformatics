def Transcribing_DNA_into_RNA(genome):
    for gen in genome:
        genome[gen] = genome[gen].replace('T', 'U')
    return genome
