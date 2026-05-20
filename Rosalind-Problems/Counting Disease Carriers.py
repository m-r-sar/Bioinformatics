def function(A):
    results = []
    for q in A:
        p = 1 - q**0.5
        prob = 1 - p**2
        results.append(round(prob,3))
    return results