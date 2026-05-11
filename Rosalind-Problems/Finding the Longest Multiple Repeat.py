from collections import defaultdict

def function(s, k, tree):
    graph = defaultdict(list)

    parents = set()

    for edge in tree:
        parent, child, loc, length = edge.split()
        graph[parent].append((child, int(loc) - 1, int(length)))
        parents.add(parent)

    best_substring = ""

    def dfs(node, current_substring):
        nonlocal best_substring

        if node not in parents:
            return 1

        total_leaves = 0

        for child, loc_start, length in graph[node]:
            edge_string = s[loc_start: loc_start + length]
            new_substring = current_substring + edge_string

            total_leaves += dfs(child, new_substring)

        if total_leaves >= k:
            if len(current_substring) > len(best_substring):
                best_substring = current_substring

        return total_leaves

    dfs("node1", "")

    return best_substring
