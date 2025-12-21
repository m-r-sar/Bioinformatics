def Consensus_and_Profile(dataset):
    dataset = list(dataset.values())
    length = len(dataset[0])

    #Profile matrix
    A_list = [0 for _ in range(length)]
    C_list = [0 for _ in range(length)]
    G_list = [0 for _ in range(length)]
    T_list = [0 for _ in range(length)]

    for data in dataset:
        i = 0
        for char in data:
            if char == "A":
                A_list[i] += 1
            elif char == "T":
                T_list[i] += 1
            elif char == "C":
                C_list[i] += 1
            elif char == "G":
                G_list[i] += 1
            i += 1
    profile = {"A": A_list, "C": C_list, "G": G_list, "T": T_list}

    #Consensus string
    consensus = ""
    for row in range(length):
        temp = []
        for col in profile:
            temp.append(profile[col][row])

        index = temp.index(max(temp))
        if index == 0:
            consensus += "A"
        elif index == 1:
            consensus += "C"
        elif index == 2:
            consensus += "G"
        elif index == 3:
            consensus += "T"

    return profile, consensus

# profile, consensus = Consensus_and_Profile(Parse_FASTA("FASTA_Rosalind"))
# print(consensus)
# for char, values in profile.items():
#     formatted_values = " ".join(map(str, values))
#     print(f"{char}: {formatted_values}")
