def Counting_Point_Mutations(string_1, string_2):
    hamming_distance = 0
    for i in range(len(string_1)):
        if not(string_1[i] == string_2[i]):
            hamming_distance += 1
    return hamming_distance
