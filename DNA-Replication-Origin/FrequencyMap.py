def FrequencyMap(text, k):
    kMers = {}
    n = len(text)
    for i in range(n - k + 1):
        Pattern = text[i:i + k]
        count = 0
        for i in range(n - len(Pattern) + 1):
            if text[i:i + len(Pattern)] == Pattern:
                count = count + 1
        kMers[Pattern] = count
    return kMers
