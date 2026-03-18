def Complementing_a_Strand_of_DNA(genome):
    new_genome = []
    for letter in genome:
        if letter == "A":
            new_genome.append("T")
        elif letter == "T":
            new_genome.append("A")
        elif letter == "C":
            new_genome.append("G")
        elif letter == "G":
            new_genome.append("C")
    new_genome.reverse()
    new_genome = ''.join(new_genome)
    return new_genome

def function(dataset):
    dataset = list(dataset.values())
    reverse_complements = [Complementing_a_Strand_of_DNA(s) for s in dataset]
    uniques = []
    repeats = []
    not_in_uniques = []
    corrections = {}
    for reed in dataset:
        if reed not in uniques:
            uniques.append(reed)
        else:
            repeats.append(reed)
            not_in_uniques.append(reed)

    for i in range(len(repeats)):
        if repeats[i] in uniques:
            uniques.remove(repeats[i])
    for i in range(len(dataset)):
        if reverse_complements[i] in uniques:
            uniques.remove(reverse_complements[i])
            not_in_uniques.append(reverse_complements[i])

    def get_hamming_distance(a, b):
        if sum(1 for char_a, char_b in zip(a, b) if char_a != char_b) == 1:
            return True
        else:
            return False

    reversed_not_in_uniques = [Complementing_a_Strand_of_DNA(s) for s in not_in_uniques]
    for uni in uniques:
        flag = False
        for s in not_in_uniques:
            if get_hamming_distance(uni, s):
                corrections[uni] = s
                flag = True
                break
        if not flag:
            for s in reversed_not_in_uniques:
                if get_hamming_distance(uni, s):
                    corrections[uni] = s
                    break

    return corrections

# for key in corrections:
#     print(f"{key}->{corrections[key]}")
