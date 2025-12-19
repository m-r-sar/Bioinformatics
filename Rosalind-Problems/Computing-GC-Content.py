def Computing_GC_Content(dataset, id_s, id_l, name):
    parsed_dataset = {}
    for string in dataset:
        count = 0
        string_id = string[id_s-1:id_l-1]
        genome = string[id_l-1:]
        for l in genome:
            if l == "G":
                count += 1
            elif l == "C":
                count += 1
        GC = (count*100) / len(genome)
        parsed_dataset[string_id] = CG
    inverse = [(value, key) for key, value in parsed_dataset.items()]
    answer = max(inverse)
    return f"{name}_{answer[1]} \n{answer[0]}"


def Parse_FASTA(filename):
    string = []
    with open(filename) as file:
        for line in file:
            string.append(line)
            print(line)
    print(string)
    string = ''.join(string)
    string = string.split('\n')
    string = ''.join(string)
    string = string.split(">")
    string.remove(string[0])
    return string

#dataset = Parse_FASTA("FASTA_Rosalind")
#print(Computing_GC_Content(dataset, 10, 14, "Rosalind"))
