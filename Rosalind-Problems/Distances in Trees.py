from collections import deque

def parse_newick(newick_string):
    """
    Parses a Newick string into an adjacency list
    Returns the graph and a mapping of node names to their integer IDs.
    """
    graph = {}
    names_to_id = {}
    stack = []

    current_id = 0
    graph[current_id] = []
    next_id = 1

    i = 0
    while i < len(newick_string):
        char = newick_string[i]

        if char == '(':
            # Moving down: create a child node
            stack.append(current_id)
            new_node = next_id
            next_id += 1
            graph[new_node] = []

            # Add undirected edge
            graph[current_id].append(new_node)
            graph[new_node].append(current_id)

            current_id = new_node
            i += 1

        elif char == ',':
            # Moving sideways: create a sibling node
            parent_id = stack[-1]
            new_node = next_id
            next_id += 1
            graph[new_node] = []

            # Add undirected edge to parent
            graph[parent_id].append(new_node)
            graph[new_node].append(parent_id)

            current_id = new_node
            i += 1

        elif char == ')':
            # Moving up: return to parent node
            current_id = stack.pop()
            i += 1

        elif char == ';':
            break

        elif char.isspace():
            i += 1

        else:
            name = ""
            while i < len(newick_string) and newick_string[i] not in '(),; \n':
                name += newick_string[i]
                i += 1

            if name:
                names_to_id[name] = current_id

    return graph, names_to_id


def bfs_distance(graph, start_id, end_id):
    """
    Uses Breadth-First Search to find the shortest path between two node IDs.
    """
    if start_id == end_id:
        return 0

    # Queue stores tuples of (current_node_id, distance_from_start)
    queue = deque([(start_id, 0)])
    visited = {start_id}

    while queue:
        current, dist = queue.popleft()

        if current == end_id:
            return dist

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))


def solve_newick_distances(input_data):
    """
    Parses the full input dataset and returns the final space-separated string of distances.
    """
    lines = [line.strip() for line in input_data.strip().split('\n') if line.strip()]
    results = []

    # Process input in pairs: index `i` is the tree, `i+1` are the target nodes
    for i in range(0, len(lines), 2):
        newick = lines[i]
        nodes = lines[i + 1].split()

        if len(nodes) != 2:
            continue

        node_x, node_y = nodes[0], nodes[1]

        # 1. Build the graph
        graph, names_to_id = parse_newick(newick)

        # 2. Look up the IDs for the requested nodes
        start_id = names_to_id[node_x]
        end_id = names_to_id[node_y]

        # 3. Calculate distance
        dist = bfs_distance(graph, start_id, end_id)
        results.append(str(dist))

    return " ".join(results)
