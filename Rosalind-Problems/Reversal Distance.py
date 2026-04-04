from collections import deque
import itertools

def function(keys, reversals):
    reversals_counts = []

    def bfs(start, goal):
        if start == goal:
            return 0

        n = len(start)
        visited = {start: 0}
        queue = deque([start])

        while queue:
            current_vertex = queue.popleft()
            current_steps = visited[current_vertex]

            for i, j in itertools.combinations(range(n + 1), 2):
                if j - i <= 1:
                    continue

                copy = (
                        current_vertex[:i] +
                        current_vertex[i:j][::-1] +
                        current_vertex[j:]
                )

                if copy not in visited:
                    visited[copy] = current_steps + 1

                    if copy == goal:
                        return visited[copy]

                    queue.append(copy)

    for key, reversal in zip(keys, reversals):
        reversals_counts.append(bfs(reversal, key))

    return reversals_counts
