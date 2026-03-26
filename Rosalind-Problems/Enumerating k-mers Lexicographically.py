def function(a, n):
    if n == 1:
        for x in a:
            yield [x]
    else:
        for i in range(len(a)):
            for x in function(a[:i] + a[i:], n - 1):
                yield [a[i]] + x
