class Solution {
public:
    int maxIncreasingCells(vector<vector<int>>& mat) {
        int n = mat.size(), m = mat[0].size();
        vector<int> rowMax(n), colMax(m);
        map<int, vector<pair<int, int>>> pos;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                pos[mat[i][j]].push_back({i, j});
            }
        }
        int ans = 0;

        for (auto& [num, cells]: pos) {
            int k = cells.size();

            vector<int> next(k);
            for (int i = 0; i < k; ++i) {
                int r = cells[i].first, c = cells[i].second;
                next[i] = max(rowMax[r], colMax[c]) + 1;
                ans = max(ans, next[i]);
            }
            for (int i = 0; i < k; ++i) {
                int r = cells[i].first, c = cells[i].second;
                rowMax[r] = max(rowMax[r], next[i]);
                colMax[c] = max(colMax[c], next[i]);
            }
        }
        return ans;
    }
};