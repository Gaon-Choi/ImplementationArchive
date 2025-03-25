def BFS(graph, v):
    result = []
    visited = [False] * len(graph)

    visited[v] = True
    queue = [v]
	
    while queue:
        vertex = queue.pop(0)
        result.append(vertex)

        for curr_v in sorted(graph[vertex]):
            if not visited[curr_v]:
                visited[curr_v] = True
                queue.append(curr_v)
                
    return result
