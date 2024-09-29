class Solution {
public:
    vector<int> validSequence(string word1, string word2) {
        int n = word1.length();
        int m = word2.length();

        vector<int> dp(n + 1, 0);
        for (int i = n - 1; i >= 0; --i) {
            dp[i] = dp[i + 1];
            if (dp[i + 1] < m && word1[i] == word2[m - dp[i + 1] - 1]) {
                dp[i]++;
            }
        }

        vector<int> ans;
        bool free = true;
        for (int i = 0; i < n; ++i) {
            if (ans.size() == m) {
                break;
            }
            if (word1[i] == word2[ans.size()]) {
                ans.push_back(i);
            } else if (free && ans.size() + 1 + dp[i + 1] >= m) {
                if (ans.empty()) {
                    ans.push_back(i);
                } else {
                    ans.push_back(ans.back() + 1);
                }
                free = false;
            }
        }
        if (ans.size() != m) {
            return {};
        }
        return ans;
    }
};