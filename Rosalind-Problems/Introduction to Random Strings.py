import math
def function(s, A):
    B = []
    for x in A:
        total = 1
        gc_probability = x / 2
        at_probability = (1-x) / 2
        for char in s:
            if char == "A" or char == "T":
                total *= at_probability
            else:
                total *= gc_probability
        B.append(round(math.log(total, 10), 4))
    return B
