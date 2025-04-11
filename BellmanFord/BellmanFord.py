def BellmanFord(graph, start):
    '''
    graph   : 인접 리스트 - list of (v, cost)
    return  : 모든 정점 쌍의 최단 거리 dist[i][j]
    '''

    '''
    [*] 개요
        - 단일 출발점으로부터의 최단 경로
        - 음수 가중치 간선 허용
        - 음수 사이클 존재 여부도 판단 가능

        - 거리 배열 dist를 ∞로 초기화, 시작점은 0으로 설정.
        - V-1번 모든 간선을 순회하며 최단 거리 갱신.
        - 마지막으로 한 번 더 순회해서 갱신이 발생하면 음수 사이클 존재.

    [*] 시간 복잡도
        - O(V * E) (V: 정점 개수, E: 간선 개수) → 간선 수가 많을 경우 느릴 수 있음
    '''

    INF = float('inf')
    
    size = len(graph)
    dist = [INF] * (size)

    # 시작점에서의 비용은 0으로 설정
    dist[start] = 0

    # 정점의 개수만큼 반복
    for _ in range(size - 1):
        for u in range(1, size):
            for v, w in graph[u]:
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

    # 음수 사이클 탐지
    for u in range(1, size):
        for v, w in graph[u]:
            if dist[u] != INF and dist[u] + w < dist[v]:
                # 음수 가중치 사이클 발견되는 경우
                return None
            
    return dist[1:]