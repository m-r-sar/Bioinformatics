def function(genome):
    gens = list(genome.values())
    superstring = gens.pop(0)

    def get_overlap(s1, s2):
        for i in range(len(s1), len(s2)//2, -1):
            if s2.startswith(s1[-i:]):
                return s1 + s2.removeprefix(s1[-i:])
        return s1

    def get_start_overlap(s1, s2):
        for i in range(len(s1), len(s2)//2, -1):
            if s2.endswith(s1[:i]):
                return s2.removesuffix(s1[:i]) + s1
        return s1

    while gens:
        for gen in gens:
            superstring = get_overlap(superstring, gen)
            superstring = get_start_overlap(superstring, gen)
        gens = [gen for gen in gens if gen not in superstring]

    return superstring
