amino_acids = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
amino_acid_masses = [71.03711, 103.00919, 115.02694, 129.04259, 147.06841, 57.02146, 137.05891, 113.08406, 128.09496, 113.08406, 131.04049, 114.04293, 97.05276, 128.05858, 156.10111, 87.03203, 101.04768, 99.06841, 186.07931, 163.06333]

def get_amino_acid(mass_diff):
    for i, a_mass in enumerate(amino_acid_masses):
        if abs(mass_diff - a_mass) < 0.01:
            return amino_acids[i]
    return None


def function(nodes):
    edges = {}

    for node in nodes:
        for next_node in nodes:
            if next_node > node:
                aa = get_amino_acid(next_node - node)
                if aa:
                    if node not in edges:
                        edges[node] = []
                    edges[node].append((next_node, aa))

    paths = []

    def dfs(current_node, path):
        paths.append(path)

        if current_node in edges:
            for next_node, aa in edges[current_node]:
                dfs(next_node, path + aa)

    for start_node in nodes:
        dfs(start_node, "")

    return max(paths, key=len)