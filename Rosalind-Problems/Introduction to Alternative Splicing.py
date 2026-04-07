import math
def function(n, k):
    total = 0
    for i in range(k, n+1):
        total += math.comb(n, i)

    return total % 1000_000
