import math

def function(n):
    result = []
    p = 1 / 2
    n = n * 2

    for k in range(1, n + 1):
        prob = 0

        for j in range(k, n + 1):
            prob += math.comb(n, j) * (p ** n)
        result.append(round(math.log10(prob), 3))

    return result
