#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;

vector<int> dijkstra(const vector<vector<pair<int, int>>> &graph, int start) {
	int graph_size = graph.size();
	
	// 거리 배열
	vector<int> dist(graph_size, INF);
	// 우선순위 큐
	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

	dist[start] = 0;
	pq.push({0, start});

	while(!pq.empty()) {
		int curr_dist = pq.top().first;
		int u = pq.top().second;
		pq.pop();

		for (const pair<int, int> adj : graph[u]) {
			int v = adj.first;
			int v_cost = adj.second;

			int new_cost = curr_dist + v_cost;
			if (new_cost < dist[v]) {
				dist[v] = new_cost;
				pq.push({new_cost, v});
			}
		}
	}

	return dist;
}
