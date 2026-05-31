def function(a):
    b = []
    for q in a:
        b.append(round(2*q * (1-q), 3))
    return b