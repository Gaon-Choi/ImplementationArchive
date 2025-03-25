import heapq

def topological_sort(graph):
    '''
    graph   : adjacency list
    '''

    # indegree array
    indegree = [0] * len(graph)

    for adj in graph:
        for v in adj:
            indegree[v] += 1

    # result of topological sort
    res = []
    pq = []

    # search for vertices with indegree 0
    for i in range(1, len(graph)):
        if indegree[i] == 0:
            heapq.heappush(pq, i)

    while pq:
        x = heapq.heappop(pq)

        res.append(x)

        # decrement indegree for each adjacent vertices
        for v in graph[x]:
            indegree[v] -= 1

            if indegree[v] == 0:
                heapq.heappush(pq, v)

    return res