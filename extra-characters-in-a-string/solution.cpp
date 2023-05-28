class Solution {
public:
    int minExtraChar(string s, vector<string>& dictionary) {
        int n = s.size();
        vector<int> dp(n + 1, 0);
        for (int i = 1; i <= n; i++) {
            dp[i] = i;
            for (int j = 0; j < i; j++) {
                string sub = s.substr(j, i - j);

                if (find(dictionary.begin(), dictionary.end(), sub) != dictionary.end()) {
                    dp[i] = min(dp[i], dp[j]);
                }
                else {
                    dp[i] = min(dp[i], dp[j] + (i - j));
                }
            }
        }

        return dp[n];
    }
};