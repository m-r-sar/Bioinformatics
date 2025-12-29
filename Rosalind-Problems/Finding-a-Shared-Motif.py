def Finding_a_Shared_Motif(gens):
    sequences = list(gens.values())
    shortest_value = min(sequences)
    length = len(shortest_value)

    for j in range(length-1):
        substrings = []
        for i in range(length):
            if not (i+length-j > length):
                substrings.append(shortest_value[i:i+length-j])
            else:
                break

        for substring in substrings:
            count = 0
            for gen in sequences:
                gen_count = 0
                if substring in gen:
                    gen_count += 1
                    count += 1
                else:
                    break
            if count == len(sequences):
                return substring
