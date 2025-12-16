def PatternMatching(Pattern, Genome):
    positions = []
    k = len(Pattern)
    n = len(Genome)
    for i in range(n - k + 1):
        if Genome[i:i + k] == Pattern:
            positions.append(i)
    return positions
