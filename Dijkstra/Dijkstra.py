import math
import heapq

def Dijkstra(graph, src):
    '''
    graph   : a graph with form of adjancy list (vertex, cost)
    src     : starting point (vertex)
    '''

    dist = [math.inf] * (len(graph) + 1)

    pq = []

    # 탐색을 시작할 정점에 대해 거리를 0으로 설정하고 힙에 삽입
    dist[src] = 0
    heapq.heappush(pq, (0, src))

    # 힙 내부가 비어있기 전까지 계속 반복
    while len(pq) > 0:
        curr_dist, u = heapq.heappop(pq)

        for v, cost in graph[u]:
            # 새로 갱신된 거리
            new_dist = curr_dist + cost

            # 새로 계산된 거리가 기존의 dist 배열에 저장된 거리 값보다 작은 경우 갱신
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))

    return dist