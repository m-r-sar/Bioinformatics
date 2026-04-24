import numpy as np

def function(set1, set2):
    multiset = []
    for num in set1:
        for num2 in set2:
            multiset.append(round(num - num2, 5))

    values, counts = np.unique(multiset, return_counts=True)

    index = np.argmax(counts)

    largest_muliplicity = values[index]
    frequency = counts[index]

    return frequency, largest_muliplicity
