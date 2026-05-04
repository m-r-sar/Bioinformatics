def Complementing_a_Strand_of_DNA(genome):
    new_genome = []
    for letter in genome:
        if letter == "A":
            new_genome.append("T")
        elif letter == "T":
            new_genome.append("A")
        elif letter == "C":
            new_genome.append("G")
        elif letter == "G":
            new_genome.append("C")
    new_genome.reverse()
    new_genome = ''.join(new_genome)
    return new_genome

def function(kmers):
    k = len(kmers[0])
    graph = set()
    rev_kmers = [Complementing_a_Strand_of_DNA(kmer) for kmer in kmers]
    SUS = set(kmers + rev_kmers)
    for kmer in SUS:
        edge = (kmer[:k-1], kmer[1-k:])
        graph.add(edge)

    return graph
