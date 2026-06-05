def reverse_complement(string):
    new_string = ""
    for letter in string:
        if letter == "A":
            new_string += "T"
        elif letter == "T":
            new_string += "A"
        elif letter == "G":
            new_string += "C"
        else:
            new_string += "G"

    return new_string[::-1]


def function(dataset):
    results = []
    for k in range(len(dataset[0]), 1, -1):
        kmers = []
        for data in dataset:
            rc = reverse_complement(data)
            for i in range(len(data) - k + 1):
                kmers.append(data[i:i + k])
                kmers.append(rc[i:i + k])

        prefixes = [kmer[:-1] for kmer in kmers]
        suffixes = [kmer[1:] for kmer in kmers]

        if set(prefixes) == set(suffixes):
            fixed_k = k
            graph = {kmer[:-1]: kmer[1:] for kmer in kmers}
            break


    visited = set()
    for kmer in graph:
        superstring = kmer[:fixed_k-2]
        node = kmer
        while True:
            if node in visited:
                break

            superstring += node[-1:]
            visited.add(node)
            node = graph[node]
        if not superstring == kmer[:fixed_k-2]:
            results.append(superstring[:len(superstring) - k+2])

    return min(results, key=len)




