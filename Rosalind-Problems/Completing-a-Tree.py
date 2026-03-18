#pure math solution
def function(n, pairs):
    return (n - 1) - len(pairs)

#Graph Traversal Path solution
def function_dfs(n, pairs):
    # 1. Build an adjacency list
    graph = {i: [] for i in range(1, n + 1)}
    for u, v in pairs:
        graph[u].append(v)
        graph[v].append(u)


    visited = set()
    components = 0

    # 2. DFS function to explore a whole component
    def dfs(node):
        stack = [node]
        while stack:
            curr = stack.pop()
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

    # 3. Count components
    for i in range(1, n + 1):
        if i not in visited:
            components += 1
            visited.add(i)
            dfs(i)

    return components - 1

#Parsing input
# with open("", "r") as f:
#     pairs = []
#     for line in f:
#         pairs.append([int(x) for x in line.split()])
#     n = pairs.pop(0).pop(0)
