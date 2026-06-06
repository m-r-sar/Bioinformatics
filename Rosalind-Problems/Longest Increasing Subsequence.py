def function(n, seq):
    seq = seq.split(' ')
    L = [seq[0]]

    for i in range(1, n):
        longest = ""
        for j in range(i):
            if int(seq[j]) < int(seq[i]) and len(longest.replace(" ", "")) < len(L[j].replace(" ", ""))+1:
                longest = L[j]
        L.append(longest + " " + seq[i])

    longest_increasing = max(L, key=len)

    L = [seq[0]]
    for i in range(1, n):
        longest = ""
        for j in range(i):
            if int(seq[j]) > int(seq[i]) and len(longest.replace(" ", "")) < len(L[j].replace(" ", ""))+1:
                longest = L[j]
        L.append(longest + " " + seq[i])

    longest_decreasing = max(L, key=len)

    return longest_increasing, longest_decreasing
