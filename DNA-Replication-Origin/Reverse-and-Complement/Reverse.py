def Reverse(Pattern):
    new_Pattern = []
    for letter in Pattern:
        new_Pattern.append(letter)
    new_Pattern.reverse()
    new_Pattern = ''.join(new_Pattern)
    return new_Pattern
