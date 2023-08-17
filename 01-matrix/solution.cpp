class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        int n = mat.size(), m = mat[0].size();
        deque<pair<int, int>> q;

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (mat[i][j] == 0) {
                    q.push_back({i, j});
                } else {
                    mat[i][j] = n * m;
                }
            }
        }

        vector<pair<int, int>> dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        while (!q.empty()) {
            pair<int, int> coord = q.front();
            q.pop_front();

            int i = coord.first, j = coord.second;
            for (auto [x, y] : dirs) {
                int ni = i + x, nj = j + y;
                if (ni >= 0 && ni < n && nj >= 0 && nj < m && mat[ni][nj] > mat[i][j] + 1) {
                    mat[ni][nj] = mat[i][j] + 1;
                    q.push_back({ni, nj});
                }
            }
        }

        return mat;
    }
};