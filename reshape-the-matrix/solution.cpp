class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& mat, int r, int c) {
        int n = mat.size();
        int m = mat[0].size();
        if (n * m != r * c)
            return mat;
        vector<vector<int>> ans(r, vector<int>(c));
        int x = 0, y = -1;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (y + 1 < c) {
                    ++y;
                } else {
                    y = 0;
                    ++x;
                }
                ans[x][y] = mat[i][j];
            }
        }
        return ans;
    }
};