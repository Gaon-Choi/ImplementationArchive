#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

/*
DFS는 스택을 써서 깊게 들어가고, 되돌아오며 탐색합니다.

스택은 중복된 노드가 들어갈 수 있기 때문에, 방문을 확정하기 전까지는 visited를 true로 하면 안 됩니다.

만약 스택에 넣을 때 visited를 true로 하면, 정작 더 빠른 경로로 방문할 수 있었던 기회를 놓칠 수도 있습니다.
*/

vector<int> DFS(const vector<vector<int>>& graph, int v) {
    vector<int> result;
    vector<bool> visited(graph.size(), false);
    stack<int> q;

    q.push(v);

    while (!q.empty()) {
        int vertex = q.top(); q.pop();

        if (!visited[vertex]) {
            visited[vertex] = true;
            result.push_back(vertex);

            // 이웃 노드를 역순 정렬해서 스택에 push하면 작은 번호가 먼저 pop됨
            // vector<int> neighbors = graph[v];
            // sort(neighbors.rbegin(), neighbors.rend());

            // for (auto curr_v : neighbors) {

            for (auto curr_v : graph[vertex]) {
                if (!visited[curr_v]) {
                    q.push(curr_v);
                }
            }
        }
    }

    return result;
}
