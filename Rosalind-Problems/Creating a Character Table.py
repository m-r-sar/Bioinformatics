import re
def function(newick_string):
    tokens = re.findall(r'\(|\)|,|;|[^\(\),\;\s]+', newick_string)

    taxa = sorted(list(set([t for t in tokens if t not in '(),;'])))
    n = len(taxa)

    stack = []
    clades = []


    for token in tokens:
        if token == '(':
            stack.append([])

        elif token == ')':
            current_clade = stack.pop()
            clades.append(set(current_clade))

            if stack:
                stack[-1].extend(current_clade)

        elif token not in ',;':
            if stack:
                stack[-1].append(token)

    character_table = []
    seen_splits = set()

    for clade in clades:
        if 1 < len(clade) < n - 1:
            array = tuple('1' if taxon in clade else '0' for taxon in taxa)

            inverse_array = tuple('0' if taxon in clade else '1' for taxon in taxa)

            if array not in seen_splits and inverse_array not in seen_splits:
                seen_splits.add(array)
                character_table.append("".join(array))

    return character_table
