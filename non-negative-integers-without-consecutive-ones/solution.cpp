class Solution {
public:
    vector<vector<vector<int>>> dp;
    int n;
    int max_bit_len;

    int dfs(int i, int prev_bit, int limit_flag) {
        if (i == max_bit_len) return 1;
        if (dp[i][prev_bit][limit_flag] != -1) return dp[i][prev_bit][limit_flag];

        int ans = 0;
        int cur_bit_limit = 9;
        if (limit_flag == 0) {
            cur_bit_limit = n & (1 << (max_bit_len - i - 1));
        }
        
        if (cur_bit_limit == 0) {
            ans += dfs(i + 1, 0, limit_flag);
        } else {
            ans += dfs(i + 1, 0, 1);
        }
        
        if (prev_bit == 0) {
            if (cur_bit_limit != 0) {
                ans += dfs(i + 1, 1, limit_flag);
            }
        }
        
        return dp[i][prev_bit][limit_flag] = ans;
    }

    int findIntegers(int num) {
        n = num;
        max_bit_len = log2(num) + 1;
        dp.resize(max_bit_len, vector<vector<int>>(2, vector<int>(2, -1)));
        return dfs(0, 0, 0);
    }
};