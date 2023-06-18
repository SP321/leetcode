class Solution {
public:
    int countPaths(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        int mod = 1e9 + 7;

        vector<vector<int>> dp(n, vector<int>(m, 1));
        vector<pair<int, pair<int, int>>> a;

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                a.push_back({grid[i][j], {i, j}});
            }
        }
        sort(a.begin(), a.end());
        long long ans=0; 
        for (const auto& x : a) {
            int val = x.first;
            int i = x.second.first;
            int j = x.second.second;

            vector<pair<int, int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
            for (const auto& dir : directions) {
                int x = i + dir.first;
                int y = j + dir.second;
                if (x >= 0 && y >= 0 && x < n && y < m && grid[x][y] > val) {
                    dp[x][y] = (dp[x][y] + dp[i][j]) % mod;
                }
            }
            ans += dp[i][j];
        }
        return ans % mod;
    }
};