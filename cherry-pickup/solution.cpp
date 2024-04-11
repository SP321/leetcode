class Solution {
public:
    int cherryPickup(vector<vector<int>>& grid) {
        int n = grid.size();
        map<int, int> memo;

        function<int(int, int, int)> dp = [&](int x1, int y1, int x2) -> int {
            int key = x1+y1*50+x2*50*50;
            if (memo.find(key) != memo.end()) 
                return memo[key];
            int y2 = x1 + y1 - x2;
            if (x1 >= n || x2 >= n || y1 >= n || y2 >= n || grid[x1][y1] == -1 || grid[x2][y2] == -1)
                return -n * n;
            if (x1 == n - 1 && x2 == n - 1 && y1 == n - 1)
                return grid[x1][y1];
            int cur = grid[x1][y1];
            if (x1 != x2)
                cur += grid[x2][y2];
            int ans = -n * n;
            vector<int> dx = {0, 1};
            vector<int> dy = {1, 0};
            for (int i = 0; i < 2; ++i) {
                for (int j = 0; j < 2; ++j) {
                    int ax = x1 + dx[i], ay = y1 + dy[i];
                    int bx = x2 + dx[j], by = y2 + dy[j];
                    ans = max(ans, dp(ax, ay, bx));
                }
            }
            return memo[key] = ans + cur;
        };
        return max(dp(0, 0, 0), 0);
    }
};