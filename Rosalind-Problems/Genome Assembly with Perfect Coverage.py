def function(dataset):
    graph = {}

    for data in dataset:
        kmer1 = data[0:-1]
        kmer2 = data[1:]

        graph[kmer1] = kmer2
        if kmer2 not in graph:
            graph[kmer2] = ""

    superstring = list(graph.keys())[0]
    kmer = list(graph.keys())[0]

    for i in range (len(graph)):
        superstring += graph[kmer][-1:]
        kmer = graph[kmer]



    return superstring[:len(superstring)-len(kmer)]