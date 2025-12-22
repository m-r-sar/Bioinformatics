import matplotlib.pyplot as plt

def Parse_FASTA(filename):
    result = {}
    string = []
    with open(filename) as file:
        for line in file:
            string.append(line)
    string = ''.join(string)
    string = string.split(">")
    string.remove(string[0])
    for s in string:
        s = s.split('\n')
        s[1] = "".join(s[1:])
        result.update({s[0]: s[1]})
    return result

def Length_Vizualization(genome):
    for gen in genome:
        genome[gen] = len(genome[gen])

    ids = list(genome.keys())
    lengths = list(genome.values())

    plt.figure(figsize=(10, 6))

    plt.barh(ids, lengths, color='skyblue')
    plt.xlabel('Gen length (bp)')
    plt.show()
