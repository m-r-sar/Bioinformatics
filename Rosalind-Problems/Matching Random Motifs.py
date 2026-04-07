def function(n, gc_probability, s):
    total = 1
    at_probability = (1 - gc_probability) / 2
    gc_probability = gc_probability / 2

    for char in s:
        if char == "A" or char == "T":
            total *= at_probability
        else:
            total *= gc_probability
    return round(1 - (1 - total)**n, 3)
