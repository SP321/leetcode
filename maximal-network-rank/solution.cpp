class Solution {
public:
    int maximalNetworkRank(int n, vector<vector<int>>& roads) {
        vector<int> count(n, 0);
        set<pair<int, int>> direct;
        for (const auto& road : roads) {
            int a = road[0], b = road[1];
            count[a]++;
            count[b]++;
            direct.insert({a, b});
            direct.insert({b, a});
        }

        int ans = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                int rank = count[i] + count[j];
                if (direct.find({i, j}) != direct.end()) {
                    rank--;
                }
                ans = max(ans, rank);
            }
        }

        return ans;
    }
};