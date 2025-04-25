#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> combination(const vector<int>& arr, int k) {
	vector<int> temp;
	vector<vector<int>> res;

	function<void(int)> backtrack = [&](int start) {
		if (temp.size() == k) {
			res.push_back(temp);
			return;
		}

		for (int i = start; i < arr.size(); ++i) {
			temp.push_back(arr[i]);
			backtrack(i + 1);
			temp.pop_back();
		}
	};

	backtrack(0);

	return res;
}
