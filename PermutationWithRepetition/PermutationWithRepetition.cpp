#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> permutation_with_repetition(const vector<int>& arr, int k) {
	vector<int> temp;
	vector<vector<int>> res;

	function<void()> backtrack = [&]() {
		if (temp.size() == k) {
			res.push_back(temp);
			return;
		}

		for (int i = 0; i < arr.size(); ++i) {
			temp.push_back(arr[i]);
			backtrack();
			temp.pop_back();
		}
	};

	backtrack();

	return res;
}
