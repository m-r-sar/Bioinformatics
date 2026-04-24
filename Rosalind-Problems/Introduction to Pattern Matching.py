def function(strings):
    tree = {1: {}}
    node_counter = 1
    adjacency_list = []

    for s in strings:
        current_node = 1

        for char in s:
            if char not in tree[current_node]:
                node_counter += 1
                adjacency_list.append((current_node, node_counter, char))
                tree[current_node][char] = node_counter

                tree[node_counter] = {}

            current_node = tree[current_node][char]

    return adjacency_list
