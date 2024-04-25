class Solution {
public:
    int longestIdealString(string s, int k) {
        vector<int> dp(128);
        for (char i : s) {
            int c = 0;
            for (int j = max(0, i - k); j <= min(127, i + k); ++j) {
                c = max(c, dp[j]);
            }
            dp[i] = c + 1;
        }
        return *max_element(dp.begin(), dp.end());
    }
};