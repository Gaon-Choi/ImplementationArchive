#include <iostream>
#include <vector>
#include <queue>
#include <climits>
#include <tuple>

using namespace std;

vector<int> Dijkstra(const vector<vector<pair<int, int>>>& graph, int src) {
    int n = graph.size(); // 정점 개수
    vector<int> dist(n, INT_MAX); // 거리 배열 (INT_MAX로 초기화)

    // 최소 힙 (거리, 정점)
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;

    // 탐색을 시작할 정점에 대해 거리를 0으로 설정하고 힙에 삽입
    dist[src] = 0;
    pq.push({0, src});

    // 힙 내부가 비어있기 전까지 계속 반복
    while (!pq.empty()) {
        int curr_dist = pq.top().first;
        int u = pq.top().second;
        pq.pop();

        // 이미 더 짧은 거리로 방문했다면 스킵
        if (curr_dist > dist[u]) continue;

        for (const pair<int, int>& p : graph[u]) {
            int v = p.first, cost = p.second;

            // 새로 갱신된 거리
            int new_dist = curr_dist + cost;

            // 새로 계산된 거리가 기존의 dist 배열에 저장된 거리 값보다 작은 경우 갱신
            if (new_dist < dist[v]) {
                dist[v] = new_dist;
                pq.push({new_dist, v});
            }
        }
    }

    return dist;
}
