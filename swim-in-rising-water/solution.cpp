class Solution {
public:
    int swimInWater(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<pair<int, int>> moves = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        
        set<pair<int, int>> visited;
        
        priority_queue<tuple<int, int, int, int>, vector<tuple<int, int, int, int>>, greater<tuple<int, int, int, int>>> pq;
        pq.push(make_tuple(grid[0][0], grid[0][0], 0, 0));
        
        while (!pq.empty()) {
            auto [max_val_so_far, val, x, y] = pq.top();
            pq.pop();
            
            if (x == n - 1 && y == n - 1) {
                return max_val_so_far;
            }
            
            for (auto [dx, dy] : moves) {
                int nx = x + dx;
                int ny = y + dy;
                
                if (nx >= 0 && nx < n && ny >= 0 && ny < n && visited.find({nx, ny}) == visited.end()) {
                    visited.insert({nx, ny});
                    pq.push(make_tuple(max(max_val_so_far, grid[nx][ny]), grid[nx][ny], nx, ny));
                }
            }
        }
        
        return -1;
    }
};