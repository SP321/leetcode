class Solution {
public:
    int minimumObstacles(vector<vector<int>>& grid) {
         int n = grid.size();
        int m = grid[0].size();
        deque<pair<int, pair<int, int>>> q;
        vector<vector<int>> dist(n, vector<int>(m, INT_MAX));
        
        q.push_back({0, {0, 0}});
        dist[0][0] = 0;

        vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};

        while (!q.empty()) {
            auto [d, node] = q.front();
            q.pop_front();

            int x = node.first;
            int y = node.second;

            if (dist[x][y] != d) continue;

            if (x == n - 1 && y == m - 1) return d;

            for (auto& [dx, dy] : directions) {
                int nx = x + dx;
                int ny = y + dy;

                if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                    int newDist = d + grid[nx][ny];
                    if (dist[nx][ny] > newDist) {
                        dist[nx][ny] = newDist;
                        if (grid[nx][ny] == 1) {
                            q.push_back({newDist, {nx, ny}});
                        } else {
                            q.push_front({newDist, {nx, ny}});
                        }
                    }
                }
            }
        }

        return -1;
    }
};