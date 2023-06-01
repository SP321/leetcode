class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int n = grid.size();
        if (grid[0][0] || grid[n - 1][n - 1]) {
            return -1;
        }
        queue<tuple<int, int, int>> q;
        q.push({0, 0, 1});
        grid[0][0] = 1;
        vector<vector<int>> directions = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}, {-1, -1}, {-1, 1}, {1, -1}, {1, 1}};
        while (!q.empty()) {
            auto [x, y, d] = q.front();
            q.pop();
            if (x == n - 1 && y == n - 1) {
                return d;
            }
            for (const auto& dir : directions) {
                int nx = x + dir[0], ny = y + dir[1];
                if (nx >= 0 && nx < n && ny >= 0 && ny < n && !grid[nx][ny]) {
                    grid[nx][ny] = 1;
                    q.push({nx, ny, d + 1});
                }
            }
        }
        return -1;
    }
};