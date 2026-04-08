def function(n, s, A):
    results = []
    for num in A:
        total = 1
        at_probability = (1 - num) / 2
        gc_probability = num / 2

        for char in s:
            if char == "A" or char == "T":
                total *= at_probability
            else:
                total *= gc_probability
        results.append(round(total*(n-len(s)+1), 3))
    return results
