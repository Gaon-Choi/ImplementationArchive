#include <bits/stdc++.h>
using namespace std;

vector<int> topological_sort(const vector<vector<int>>& graph) {
	int n = graph.size();
    // 진입 차수 배열
	vector<int> indegree(n, 0);
    // 위상 정렬 결과
	vector<int> res;
    // 우선순위 큐 (min heap)
	priority_queue<int, vector<int>, greater<int>> pq;

    // 진입 차수 배열 값 계산
	for (int u = 1; u < n; ++u) {
		for (int v : graph[u]) {
			indegree[v]++;
		}
	}

    // 진입차수가 0인 모든 간선을 우선순위 큐에 넣음
	for (int i = 1; i < n; ++i) {
		if (indegree[i] == 0) {
			pq.push(i);
		}
	}

	while (!pq.empty()) {
		int u = pq.top(); pq.pop();

		res.push_back(u);

        // 인접한 간선마다 진입 차수를 1만큼 감소
		for (int v : graph[u]) {
			indegree[v]--;
            // 진입차수가 0이 되면 우선순위 큐에 넣음
			if (indegree[v] == 0) {
				pq.push(v);
			}
		}
	}

	return res;
}
