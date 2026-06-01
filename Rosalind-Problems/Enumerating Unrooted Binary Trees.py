def insert_taxon(tree, taxon):
    trees = [(tree, taxon)]

    if isinstance(tree, tuple):
        left, right = tree
        for new_left in insert_taxon(left, taxon):
            trees.append((new_left, right))
        for new_right in insert_taxon(right, taxon):
            trees.append((left, new_right))

    return trees


def format_newick(tree):
    if isinstance(tree, str):
        return tree
    return f"({format_newick(tree[0])},{format_newick(tree[1])})"


def function(taxa_string):
    taxa = taxa_string.strip().split()
    anchor = taxa[0]
    remaining_taxa = taxa[1:]

    current_trees = [remaining_taxa[0]]
    for taxon in remaining_taxa[1:]:
        next_generation = []
        for tree in current_trees:
            next_generation.extend(insert_taxon(tree, taxon))
        current_trees = next_generation

    results = []
    for tree in current_trees:
        if isinstance(tree, tuple):
            left = format_newick(tree[0])
            right = format_newick(tree[1])
            newick_str = f"({left},{right},{anchor});"
        else:
            newick_str = f"({tree},{anchor});"

        results.append(newick_str)

    return results

