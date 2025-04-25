#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;
int n, m, src, tgt, cost;

vector<vector<int>> floyd_warshall(const vector<vector<pair<int, int>>> & graph) {
	int n = graph.size();

    // 최단 거리 행렬
	vector<vector<int>> dist(n, vector<int> (n, INF));

    // 시작 정점과 도착 정점이 같은 경우 거리는 0으로 초기화
	for (int i = 1; i < n; ++i) {
		for (int j = 1; j < n; ++j) {
			if (i != j)	continue;
			dist[i][j] = 0;
		}
	}

    // 주어진 그래프로부터 거리 정보 갱신
	for (int src = 1; src < n; ++src) {
		for (pair<int, int> p : graph[src]) {
            // 도착 지점, 간선의 가중치
            int tgt = p.first, cost = p.second;
			dist[src][tgt] = min(dist[src][tgt], cost);
		}
	}

	for (int k = 1; k < n; ++k) {
		for (int i = 1; i < n; ++i) {
			for (int j = 1; j < n; ++j) {
				if (dist[i][k] != INF && dist[k][j] != INF) {
                    // 기존 거리보다 작은 경우 갱신
					dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
				}
			}
		}
	}

	return dist;
}