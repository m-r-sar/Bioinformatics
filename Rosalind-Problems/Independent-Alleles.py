import math

def function(k, N):
    n = 2**k
    A = 0
    for i in range(0, N):
        if math.comb(n, i) == 0:
            A += (3**(n-i)) / (4**n)
        else:
            A += math.comb(n, i) * (3**(n-i)) / (4**n)

    chance = 1 - A
    return chance
