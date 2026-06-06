def function(reads):
    if not reads:
        return []

    total_edges = len(reads)
    results = set()

    def dfs(current_node, current_string, edges_count, used_edges):
        if used_edges == total_edges:
            if current_node == reads[0][:-1]:
                results.add(current_string[:total_edges])
            return

        for char in ['A', 'C', 'G', 'T']:
            next_edge = current_node + char

            if edges_count.get(next_edge, 0) > 0:
                edges_count[next_edge] -= 1

                dfs(next_edge[1:], current_string + char, edges_count, used_edges + 1)

                edges_count[next_edge] += 1

    first_read = reads[0]
    start_node = first_read[1:]
    start_string = first_read

    edges_count = {edge : reads.count(edge) for edge in reads}
    edges_count[first_read] -= 1

    dfs(start_node, start_string, edges_count, 1)

    return list(results)


dataset = []
with open(r"C:\Users\rodio\PycharmProjects\Bioinformatics\Rosalind.txt", "r") as f:
    for line in f:
        dataset.append(line.strip())
result = function(dataset)
for r in result:
    print(r)