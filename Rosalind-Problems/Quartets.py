import itertools

def function(c):
    taxa = c[0].split(' ')
    cases = c[1:]
    quartets = set()

    for case in cases:
        set0 = set()
        set1 = set()

        for i in range(len(case)):
            if case[i] == '0':
                set0.add(taxa[i])
            elif case[i] == '1':
                set1.add(taxa[i])

        if len(set0) > 1 and len(set1) > 1:
            comb0 = list(itertools.combinations(set0, 2))
            comb1 = list(itertools.combinations(set1, 2))
            for quar in itertools.product(comb0, comb1):
                pair0 = tuple(sorted(quar[0]))
                pair1 = tuple(sorted(quar[1]))

                quartet = tuple(sorted([pair0, pair1]))
                quartets.add(quartet)

    return quartets