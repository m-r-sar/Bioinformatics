def function(dataset):

    def get_hamming_distance(s1, s2):
        hamming_distance = 0
        for i in range(len(s1)):
            if not (s1[i] == s2[i]):
                hamming_distance += 1
        return hamming_distance

    dataset = list(dataset.values())
    matrix = [[] for i in range(len(dataset))]
    length = len(dataset[0])

    for i in range(0, len(dataset)):
        for j in range(0, len(dataset)):
            matrix[i].append(get_hamming_distance(dataset[i], dataset[j]) / length)

    return matrix
