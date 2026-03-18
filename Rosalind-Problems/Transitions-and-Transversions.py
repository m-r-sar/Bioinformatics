def function(s1, s2):
    transition_count = 0
    transversion_count = 0
    transition_pairs = [("A","G"), ("G","A"), ("C","T"), ("T","C")]
    pairs = []

    for i in range(len(s1)):
        if not (s1[i] == s2[i]):
            pairs.append((s1[i], s2[i]))

    for i in range(len(pairs)):
        if pairs[i] in transition_pairs:
            transition_count += 1
        else:
            transversion_count += 1

    return transition_count/transversion_count
