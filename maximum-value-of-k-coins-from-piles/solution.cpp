class Solution {
public:
    int maxValueOfCoins(vector<vector<int>>& a, int k) {
        int n = a.size();
        vector<vector<int>> dp(n + 1, vector<int>(k + 1, 0));

        for (int i = 1; i <= n; ++i) {
            for (int j = 0; j <= k; ++j) {
                int no_pick = dp[i - 1][j];
                int max_with_pick = 0;
                int sum = 0;

                for (int l = 0; l < min((int)a[i - 1].size(), j); ++l) {
                    sum += a[i - 1][l];
                    max_with_pick = max(max_with_pick, sum + dp[i - 1][j - 1 - l]);
                }

                dp[i][j] = max(no_pick, max_with_pick);
            }
        }

        return dp[n][k];
    }
};
