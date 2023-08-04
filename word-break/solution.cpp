class Solution {
public:
    string s;
    set<string> wordSet;
    vector<int> dp;

    bool wordBreak(string s, vector<string>& wordDict) {
        this->s = s;
        wordSet = set<string>(wordDict.begin(), wordDict.end());
        dp = vector<int>(s.size(), -1);
        return dfs(0);
    }

    bool dfs(int i) {
        if (i == s.size()) {
            return true;
        }
        if (dp[i] != -1) {
            return dp[i];
        }
        for (int k = i + 1; k <= min(i + 21, (int)s.size()); k++) {
            if (wordSet.count(s.substr(i, k - i)) && dfs(k)) {
                return dp[i] = 1;
            }
        }
        return dp[i] = 0;
    }
};