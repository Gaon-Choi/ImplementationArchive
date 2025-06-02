#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

vector<int> BFS(const vector<vector<int>>& graph, int v) {
    vector<int> result;
    vector<bool> visited(graph.size(), false);
    queue<int> q;

    visited[v] = true;
    q.push(v);

    while (!q.empty()) {
        int vertex = q.front(); q.pop();
        result.push_back(vertex);

        // vector<int> neighbors = graph[vertex];
        // sort(neighbors.begin(), neighbors.end());

        // for (auto curr_v : neighbors) {

        for (auto curr_v : graph[vertex]) {
            if (!visited[curr_v]) {
                visited[curr_v] = true;
                q.push(curr_v);
            }
        }
    }

    return result;
}
