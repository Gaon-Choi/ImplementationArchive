#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

const ll INF = 1e10;

pair<bool, vector<ll>> bellman_ford(const vector<vector<pair<ll, ll>>> & graph, ll start_node) {
	bool is_negative_cycle = false;
	
	int n = graph.size();

	vector<ll> dist(n, INF);
	dist[start_node] = 0;

    // 정점의 개수만큼 반복
	for (int k = 1; k < n; ++k) {
		for (int u = 1; u < n; ++u) {
			for (pair<int, ll> p : graph[u]) {
				int v = p.first;
				ll cost = p.second;
                // 최단 거리 갱신
				if (dist[u] != INF && dist[u] + cost < dist[v]) {
					dist[v] = dist[u] + cost;
				}
			}
		}
	}

    // 음수 사이클 판별
	for (int u = 1; u < n; ++u) {
		for (pair<int, ll> p : graph[u]) {
			int v = p.first;
			ll cost = p.second;
			if (dist[u] != INF && dist[u] + cost < dist[v]) {
                // 더 짧은 최단 거리가 발견되는 경우 음수 사이클이 존재하는 것임
				is_negative_cycle = true;
				break;
			}
		}

		if (is_negative_cycle) break;
	}

	// 첫번째 요소 삭제
	dist = vector<ll> (dist.begin() + 1, dist.end());

	return pair<bool, vector<ll>> (is_negative_cycle, dist);
}