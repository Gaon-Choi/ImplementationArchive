import heapq

def Prim(start, graph):
    '''
    start   : the initial vertex to start mst searching
    graph   : adjacency list
    '''
    n = len(graph) - 1

    # total weight of minimum spanning tree
    mst = 0

    dist = [1e9] * (n + 1)      # distance array
    visited = [False] * (n + 1) # visit-or-not array

    pq = []

    dist[start] = 0
    heapq.heappush(pq, (0, start))

    while len(pq) > 0:
        min_dist, min_idx = heapq.heappop(pq)

        if visited[min_idx]:
            continue

        visited[min_idx] = True
        mst += min_dist

        for tgt_idx, tgt_dist in graph[min_idx]:
            if dist[tgt_idx] > tgt_dist:
                dist[tgt_idx] = tgt_dist
                heapq.heappush(pq, (dist[tgt_idx], tgt_idx))

    return mst
