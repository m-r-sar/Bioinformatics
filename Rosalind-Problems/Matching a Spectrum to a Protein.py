from collections import Counter
amino_acid_masses = {
    "A": 71.03711,
    "C": 103.00919,
    "D": 115.02694,
    "E": 129.04259,
    "F": 147.06841,
    "G": 57.02146,
    "H": 137.05891,
    "I": 113.08406,
    "K": 128.09496,
    "L": 113.08406,
    "M": 131.04049,
    "N": 114.04293,
    "P": 97.05276,
    "Q": 128.05858,
    "R": 156.10111,
    "S": 87.03203,
    "T": 101.04768,
    "V": 99.06841,
    "W": 186.07931,
    "Y": 163.06333
}

def function(proteins, r):
    best_protein = ""
    max_multiplicity = 0

    for protein in proteins:
        spec = []

        prev_mass = 0
        for i in range(len(protein) - 1):
            prev_mass += amino_acid_masses[protein[i]]
            spec.append(prev_mass)

        prev_mass = 0
        for i in range(-1, -len(protein), -1):
            prev_mass += amino_acid_masses[protein[i]]
            spec.append(prev_mass)

        differences = [round(num - s, 5) for s in spec for num in r]

        counts = Counter(differences)

        current_max = max(counts.values())

        if current_max > max_multiplicity:
            max_multiplicity = current_max
            best_protein = protein

    return max_multiplicity, best_protein