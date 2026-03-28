import math

def function(s):
    au_count = s.count("U")
    cg_count = s.count("C")

    return math.factorial(au_count) * math.factorial(cg_count)
