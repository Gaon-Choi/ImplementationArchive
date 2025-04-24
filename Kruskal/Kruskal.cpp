#include <bits/stdc++.h>
using namespace std;

vector<int> uf;
vector<tuple<int, int, int>> edges;

int n, m, start_node, end_node, cost;

bool cmp(tuple<int, int, int> a, tuple<int, int, int> b) {
	return get<2>(a) < get<2>(b);
}

int find_(int x) {
	if (x == uf[x]) {
		return x;
	}

	int root_node = find_(uf[x]);
	uf[x] = root_node;

	return root_node;
}

void union_(int a, int b) {
	int A = find_(a);
	int B = find_(b);

	uf[B] = A;
}

/**
 * @brief Kruskal 알고리즘을 이용해 그래프의 최소 신장 트리(MST)를 계산한다.
 *
 * @param v_count 그래프의 정점(vertex)의 개수 (정수형, int)
 * @param edges 그래프의 간선(edge) 리스트 (vector<tuple<int, int, int>> 타입)
 *              각 간선은 (시작 정점, 끝 정점, 간선의 가중치)의 형태로 구성된다.
 *
 * @return MST를 구성하는 모든 간선의 가중치 합계 (정수형, int)
 *
 * @note 이 함수는 간선 리스트를 직접 정렬하며, 간선 리스트가 참조로 전달되므로 호출 후 정렬 상태가 변경된다.
 */
int Kruskal(int v_count, vector<tuple<int, int, int>> &edges) {
    // 간선을 가중치(weight)의 오름차순으로 정렬
    sort(edges.begin(), edges.end(), [](const tuple<int, int, int>& a, const tuple<int, int, int>& b) {
        return get<2>(a) < get<2>(b);
    });

    int g_edge = 0;  // MST에 포함된 간선의 개수
    int mst = 0;     // MST의 가중치 합

    // 정렬된 모든 간선을 순회
    for (auto edge : edges) {
        int node_a = find_(get<0>(edge));  // 시작 정점의 루트 노드를 찾는다.
        int node_b = find_(get<1>(edge));  // 끝 정점의 루트 노드를 찾는다.
        int cost = get<2>(edge);           // 현재 간선의 가중치

        // 두 정점이 서로 다른 집합에 있다면(즉, 사이클이 아니라면) MST에 추가
        if (node_a != node_b) {
            union_(node_a, node_b);  // 두 정점의 집합을 하나로 합친다.
            mst += cost;             // MST의 가중치 합에 현재 간선의 가중치를 더한다.
            g_edge++;                // MST에 포함된 간선 개수를 증가시킨다.
        }

        // MST가 완성된 경우(정점 개수 - 1개의 간선 연결)
        if (g_edge == v_count - 1)
            break;
    }

    return mst;  // MST의 총 가중치 합을 반환
}
