class Solution {
public:
    int n;
    vector<pair<int, int>> moves = {{-1, -2}, {-2, -1}, {-2, 1}, {-1, 2}, {1, 2}, {2, 1}, {2, -1}, {1, -2}};
    map<pair<pair<int, int>, int>, double> dp;

    double dfs(int i, int j, int steps) {
        if (steps == 0) {
            return (i >= 0 && i < n && j >= 0 && j < n) ? 1.0 : 0.0;
        }
        auto it = dp.find({{i, j}, steps});
        if (it != dp.end()) {
            return it->second;
        }
        double ans = 0.0;
        for (const auto& k : moves) {
            int x = i + k.first;
            int y = j + k.second;
            if (x >= 0 && x < n && y >= 0 && y < n) {
                ans += dfs(x, y, steps - 1) / 8.0;
            }
        }
        return dp[{{i, j}, steps}] = ans;
    }
    double knightProbability(int n, int k, int row, int column) {
        this->n = n;
        return dfs(row, column, k);
    }
};