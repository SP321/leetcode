
class Solution {
public:
    string s;
    vector<vector<int>> dp;

    int dfs(int i, int j) {
        if (i > j)
            return 0;
        if (dp[i][j] != -1)
            return dp[i][j];
            
        dp[i][j] = dfs(i + 1, j) + 1;
        for (int k = i + 1; k <= j; k++) {
            if (s[i] == s[k]) {
                dp[i][j] = min(dp[i][j], dfs(i + 1, k - 1) + dfs(k, j));
            }
        }
        return dp[i][j];
    }

    int strangePrinter(string s) {
        this->s = s;
        int n = s.size();
        dp.resize(n, vector<int>(n, -1));
        return dfs(0, n - 1);
    }
};