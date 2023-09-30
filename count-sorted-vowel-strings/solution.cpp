class Solution {
public:
    int countVowelStrings(int n) {
        vector<vector<int>> dp(n, vector<int>(5, 0));

        for(int j = 0; j < 5; ++j) {
            dp[0][j] = 1;
        }

        for(int i = 1; i < n; ++i) {
            for(int j = 0; j < 5; ++j) {
                for(int k = 0; k <= j; ++k) {
                    dp[i][j] += dp[i-1][k];
                }
            }
        }

        int result = 0;
        for(int j = 0; j < 5; ++j) {
            result += dp[n-1][j];
        }
        return result;
    }
};