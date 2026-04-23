amino_acid_masses = {71.037: 'A',
                   103.009: 'C',
                   115.027: 'D',
                   129.043: 'E',
                   147.068: 'F',
                   57.021: 'G',
                   137.059: 'H',
                   113.084: 'L',
                   128.095: 'K',
                   131.04: 'M',
                   114.043: 'N',
                   97.053: 'P',
                   128.059: 'Q',
                   156.101: 'R',
                   87.032: 'S',
                   101.048: 'T',
                   99.068: 'V',
                   186.079: 'W',
                   163.063: 'Y'}


def function(l):
    result = []
    for i in range(-1, -len(l), -1):
        amino_acid = amino_acid_masses[round(l[i]-l[i-1], 3)]
        result.append(amino_acid)
    result.reverse()
    return ''.join(result)
