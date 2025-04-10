import math

def FloydWarshall(graph):
    '''
    graph   : 인접 행렬 (2차원 배열), graph[i][j]는 i에서 j로 가는 비용 (간선이 없는 경우 INF)
    return  : 모든 정점 쌍의 최단 거리 dist[i][j]
    '''

    '''
    [*] 개요
        - 모든 정점에서 모든 정점으로의 최단 거리를 구하는 알고리즘
        - 음의 간선이 있어도 작동하지만 음의 사이클이 존재하면 사용할 수 없음
        - 동적 계획법(DP)을 기반으로 구현됨

    [*] 시간 복잡도
        - O(N³) (N: 정점 개수) → 정점 수가 작을 때 사용
    '''

    size = len(graph)

    dist = [[math.inf] * size for _ in range(size)]

    # 같은 정점에서 정점까지의 거리는 0으로 설정 (자기 자신까지의 거리)
    for i in range(size):
        dist[i][i] = 0

    # 그래프에서 간선 비용 반영
    for i in range(size):
        for j in range(size):
            if graph[i][j] != math.inf:
                dist[i][j] = graph[i][j]


    # 모든 정점 쌍에 대해 최단 거리를 반복적으로 갱신
    # 중간에 k 정점을 거쳐 가는 경로와 직접 가는 경로 중 더 짧은 것을 선택
    for k in range(size):           # 경유지
        for i in range(size):       # 출발지
            for j in range(size):   # 도착지
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist