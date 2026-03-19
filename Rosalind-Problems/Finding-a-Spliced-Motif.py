def function(dataset):
    s1, s2 = list(dataset.values())
    result = []
    last_i = 0
    for symbol in s2:
        for i in range(last_i, len(s1)):
            if s1[i] == symbol:
                result.append(str(i+1))
                last_i = i + 1
                break
    return result
