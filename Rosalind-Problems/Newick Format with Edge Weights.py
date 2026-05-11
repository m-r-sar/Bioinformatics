from collections import deque


def parse_weighted_newick(newick_string):
    """
    Parses a weighted Newick string into an adjacency dictionary.
    Returns the graph (mapping nodes to neighbors and edge weights)
    and a dictionary mapping node names to their IDs.
    """
    graph = {}
    node_names = {}
    stack = []

    node_count = 0

    def get_id():
        nonlocal node_count
        node_count += 1
        return node_count

    current = get_id()
    graph[current] = {}

    i = 0
    while i < len(newick_string):
        char = newick_string[i]

        if char == '(':
            stack.append(current)
            child = get_id()
            graph[current][child] = 0
            graph[child] = {current: 0}
            current = child
            i += 1

        elif char == ',':
            parent = stack[-1]
            child = get_id()
            graph[parent][child] = 0
            graph[child] = {parent: 0}
            current = child
            i += 1

        elif char == ')':
            current = stack.pop()
            i += 1

        elif char == ';':
            break

        elif char.isspace() or char == '\n':
            i += 1

        else:
            start = i
            while i < len(newick_string) and newick_string[i] not in '(),; \n':
                i += 1
            info = newick_string[start:i]

            weight = 0.0

            if ':' in info:
                parts = info.split(':')
                name = parts[0]
                weight = int(parts[1])
            else:
                name = info

            if name:
                node_names[name] = current

            # The weight applies to the edge connecting the current node to its parent
            if stack:
                parent = stack[-1]
                graph[parent][current] = weight
                graph[current][parent] = weight

    return graph, node_names


def bfs_distance(graph, start_id, end_id):
    """
    Uses Breadth-First Search to find the shortest path between two node IDs
    in a weighted graph.
    """
    if start_id == end_id:
        return 0

    queue = deque([(start_id, 0)])
    visited = {start_id}

    while queue:
        current, dist = queue.popleft()

        if current == end_id:
            return dist

        # neighbor_dict is {neighbor_id: edge_weight}
        for neighbor, weight in graph[current].items():
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + weight))

    return -1


def solve_newick_distances(input_data):
    """
    Parses the full input dataset and returns the final space-separated string of distances.
    """
    lines = [line.strip() for line in input_data.strip().split('\n') if line.strip()]
    results = []

    for i in range(0, len(lines), 2):
        newick = lines[i]
        nodes = lines[i + 1].split()

        if len(nodes) != 2:
            continue

        node_x, node_y = nodes[0], nodes[1]

        graph, node_names = parse_weighted_newick(newick)

        start_id = node_names[node_x]
        end_id = node_names[node_y]

        dist = bfs_distance(graph, start_id, end_id)

        results.append(str(int(dist) if dist == int(dist) else dist))

    return " ".join(results)
