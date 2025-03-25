def DFS(graph, v):
    result = []
    visited = [False] * len(graph)

    stack = [v]

    while stack:
        vertex = stack.pop()
        
        if not visited[vertex]:
            visited[vertex] = True
            result.append(vertex)
            
            for curr_v in sorted(graph[vertex], reverse=True):
                if not visited[curr_v]:
                    stack.append(curr_v)
                    
    return result
