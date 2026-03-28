import math
def function(n, k):
    return (math.factorial(n) / math.factorial(n - k)) % 1000000
