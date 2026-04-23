from collections import deque
import itertools

def function(goal, start):
    if start == goal:
        return 0

    n = len(start)
    visited = {start: [0,[]]}
    queue = deque([start])

    while queue:
        current_vertex = queue.popleft()
        current_steps = visited[current_vertex][0]

        for i, j in itertools.combinations(range(n + 1), 2):

            if j - i <= 1:
                continue

            copy = (
                    current_vertex[:i] +
                    current_vertex[i:j][::-1] +
                    current_vertex[j:]
            )
            sort = [[i+1, j]]

            if copy not in visited:
                visited[copy] = [current_steps + 1, visited[current_vertex][1] + sort]

                if copy == goal:
                    return visited[copy]

                queue.append(copy)
