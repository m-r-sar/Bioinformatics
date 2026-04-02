def function(s, k):
    result = {}
    length = len(s)
    for i in range(length):
        if i+k > length:
            break
        if s[i:i+k] in result:
            result[s[i:i+k]] += 1
        else:
            result[s[i:i+k]] = 1
    return dict(sorted(result.items()))
