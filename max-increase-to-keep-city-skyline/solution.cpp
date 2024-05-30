class Solution {
public:
    int maxIncreaseKeepingSkyline(std::vector<std::vector<int>>& grid) {
        int n = grid.size();
        int ans = 0;
        vector<int> rmax(n), cmax(n);

        for (int i = 0; i < n; i++) {
            int row_max=0;
            for (int j = 0; j < n; j++) {
                row_max = max(row_max, grid[i][j]);
            }
            rmax[i] = row_max;
        }

        for (int j = 0; j < n; j++) {
            int col_max = 0;
            for (int i = 0; i < n; i++) {
                col_max = max(col_max, grid[i][j]);
            }
            cmax[j] = col_max;
        }

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                ans += min(rmax[i], cmax[j]) - grid[i][j];
            }
        }

        return ans;
    }
};