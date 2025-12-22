def Overlap_Graphs(gens, k):
    pairs = []
    keys = list(gens.keys())
    vals = list(gens.values())
    prefix_vals = [val[:k] for val in vals]

    for i in range(len(keys)):
        suf = vals[i][-k:]
        if suf in prefix_vals:
            indices = [j for j, x in enumerate(prefix_vals) if x == suf]
            for index in indices:
                pairs.append([keys[i], keys[index]])

    for pair in pairs:
        if gens[pair[0]] == gens[pair[1]]:
            pairs.remove(pair)
    return pairs
