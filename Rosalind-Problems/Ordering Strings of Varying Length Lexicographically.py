def function(a, n):
    if n > 0:
        for i in range(len(a)):
            yield [a[i]]

            for x in function(a[:i] + a[i:], n - 1):
                yield [a[i]] + x
