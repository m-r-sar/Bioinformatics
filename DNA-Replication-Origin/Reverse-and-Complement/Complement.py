def Complement(Pattern):
    new_Pattern = []
    for letter in Pattern:
        if letter == "A":
            new_Pattern.append("T")
        elif letter == "T":
            new_Pattern.append("A")
        elif letter == "C":
            new_Pattern.append("G")
        elif letter == "G":
            new_Pattern.append("C")
    new_Pattern = ''.join(new_Pattern)
    return new_Pattern
