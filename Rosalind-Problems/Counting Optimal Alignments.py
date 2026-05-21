def function(x):
    x = 2*x - 5
    total = 1
    for i in range(x, 1, -2):
        total *= i

    return total % 1000000
