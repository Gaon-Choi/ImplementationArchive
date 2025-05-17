from collections import deque

def check_bipartile(graph):
    size = len(graph)

    visited = [-1] * size

    for start_point in range(1, size):
        if visited[start_point] == -1:

            queue = deque([start_point])
            visited[start_point] = 1

            while queue:
                x = queue.popleft()

                for adj in graph[x]:
                    if visited[adj] == -1:
                        visited[adj] = visited[x] ^ 1
                        queue.append(adj)

                    elif visited[adj] == visited[x]:
                        return False
            
    return True
