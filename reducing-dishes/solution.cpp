class Solution {
public:
    int maxSatisfaction(std::vector<int>& satisfaction) {
        int n = satisfaction.size();
        sort(satisfaction.begin(), satisfaction.end());
        
        vector<vector<int>> dp(n + 2, vector<int>(n + 2, 0));
        
        for (int i = n - 1; i >= 0; i--) {
            for (int j = n; j >= 1; j--) {
                int take = dp[i + 1][j + 1] + satisfaction[i] * j;
                int leave = dp[i + 1][j];
                dp[i][j] = max(take, leave);
            }
        }
        
        return dp[0][1];
    }
};