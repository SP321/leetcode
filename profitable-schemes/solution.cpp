class Solution {
public:
    int profitableSchemes(int n, int minProfit, vector<int>& group, vector<int>& profit) {
        int m = group.size();
        int md = 1e9 + 7;
        vector<vector<vector<int>>> dp(n + 1, vector<vector<int>>(m + 1, vector<int>(minProfit + 1, 0)));
        for (int i = 0; i <= n; i++)
            dp[i][0][0] = 1;
        for (int j = 1; j <= m; j++) {
            int g = group[j - 1], p = profit[j - 1];
            for (int i = 0; i <= n; i++) {
                for (int k = 0; k <= minProfit; k++) {
                    dp[i][j][k] = dp[i][j - 1][k];
                    if (i >= g) {
                        int prev_profit = max(0, k - p);
                        dp[i][j][k] = (dp[i][j][k] + dp[i - g][j - 1][prev_profit]) % md;
                    }
                }
            }
        }
        return dp[n][m][minProfit];
    }
};