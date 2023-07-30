int md = 1e9+7;

class Solution {
public:
    vector<vector<vector<vector<int>>>> dp;
    string num1, num2;
    int min_sum, max_sum;

    int dfs(int i, int min_flag, int max_flag, int pre) {
        if (pre > max_sum) return 0;
        if (i == num2.size()) return min_sum <= pre && pre <= max_sum;
        if (dp[i][min_flag][max_flag][pre] != -1) return dp[i][min_flag][max_flag][pre];
        
        int ans = 0;
        int lo_digit = min_flag ? num1[i] - '0' : 0;
        int hi_digit = max_flag ? num2[i] - '0' : 9;

        for (int digit = lo_digit; digit <= hi_digit; digit++) {
            int next_min_flag = min_flag && (digit == lo_digit);
            int next_max_flag = max_flag && (digit == hi_digit);
            ans = (ans + dfs(i + 1, next_min_flag, next_max_flag, pre + digit)) % md;
        }

        return dp[i][min_flag][max_flag][pre] = ans;
    }

    int count(string num1, string num2, int min_sum, int max_sum) {
        this->num1 = string(num2.size() - num1.size(), '0') + num1;
        this->num2 = num2;
        this->min_sum = min_sum;
        this->max_sum = max_sum;
        dp = vector(num2.size(), vector(2, vector(2, vector(max_sum + 1, -1))));
        return dfs(0, 1, 1, 0);
    }
};