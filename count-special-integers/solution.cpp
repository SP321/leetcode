
class Solution {
public:
    vector<vector<vector<int>>> dp;
    string str_n;
    int countSpecialNumbers(int n) {
        str_n = to_string(n);
        dp.resize(str_n.size()+1, vector<vector<int>>(1024, vector<int>(2, -1)));
        return dfs(str_n.size(), 1023, true, true) - 1;
    }

    int dfs(int i, int mask, bool is_most_significant, bool is_capped) {
        if (i == 0) return 1;
        if (dp[i][mask][is_capped] != -1) return dp[i][mask][is_capped];
        int ans = 0;
        int cap = 9;
        if (is_capped) cap = str_n[str_n.size() - i] - '0';
        for (int j = 0; j <= cap; ++j) {
            if (!((mask >> j) & 1)) continue;
            bool is_capped_new = is_capped && (j == cap);
            if (j == 0 && is_most_significant) {
                ans += dfs(i - 1, mask, is_most_significant, is_capped_new);
            } else {
                int next_mask = mask & ~(1 << j);
                ans += dfs(i - 1, next_mask, false, is_capped_new);
            }
        }
        return dp[i][mask][is_capped] = ans;
    }
};