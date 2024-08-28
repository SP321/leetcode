class Solution {
public:
    int countSubIslands(vector<vector<int>>& grid1, vector<vector<int>>& grid2) {
        int m = grid1.size();
        int n = grid1[0].size();
        int ans = 0;

        auto dfs = [&](int i, int j, auto&& dfs_ref) -> int {
            static vector<pair<int, int>> dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
            for (auto [dx, dy] : dirs) {
                int x = i + dx;
                int y = j + dy;
                if (x >= 0 && x < m && y >= 0 && y < n && grid2[x][y]) {
                    if (grid1[x][y] == 0) {
                        return 0;
                    }
                    grid1[x][y] = 0;
                    grid2[x][y] = 0;
                    int res = dfs_ref(x, y, dfs_ref);
                    if (res == 0) {
                        grid2[x][y] = 1;
                        return 0;
                    }
                }
            }
            return 1;
        };

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid1[i][j] && grid2[i][j]) {
                    grid1[i][j] = 0;
                    grid2[i][j] = 0;
                    int cur = dfs(i, j, dfs);
                    if (cur == 0) {
                        grid2[i][j] = 1;
                    }
                    ans += cur;
                }
            }
        }

        return ans;
    }
};
