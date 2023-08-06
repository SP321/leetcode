class Solution {
public:
    vector<vector<int>> matrix, dp, dirs;
    int n, m;
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        this->matrix = matrix;
        n = matrix.size();
        if (n == 0) return 0;
        m = matrix[0].size();
        dp.resize(n, vector<int>(m, 0));
        dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        int res = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                res = max(res, dfs(i, j));
            }
        }
        return res;
    }

    int dfs(int i, int j) {
        if (dp[i][j] != 0) return dp[i][j];
        int ans = 1;
        for (auto& dir : dirs) {
            int x = i + dir[0], y = j + dir[1];
            if (x < 0 || x >= n || y < 0 || y >= m || matrix[x][y] <= matrix[i][j])
                continue;
            int len = 1 + dfs(x, y);
            ans = max(ans, len);
        }
        dp[i][j] = ans;
        return ans;
    }
};