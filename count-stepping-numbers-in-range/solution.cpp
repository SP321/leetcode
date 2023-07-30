
class Solution {
public:
    vector<string> maximums;
    vector<vector<vector<int>>> dp;
    int MOD = 1e9+7;

    string decrementString(string str) {
        int n = str.size();
        for(int i = n - 1; i >= 0; --i) {
            if(str[i] != '0') {
                str[i]--;
                return str;
            }
            else {
                str[i] = '9';
            }
        }
        return str[0] == '0' ? str.substr(1) : str;
    }

    int dfs(int i, int max_flag, int prev) {
        if(i==0)
            return 1;
        if(dp[i][max_flag][prev+1] != -1)
            return dp[i][max_flag][prev+1];
        int limit = 9;
        if(max_flag < 2)
            limit = maximums[max_flag][maximums[max_flag].size() - i] - '0';
        int ans = 0;
        for(int j=0; j<=limit; j++){
            if(prev == -1 || abs(prev-j) == 1){
                int next = j;
                if(prev == -1 && j == 0)
                    next = -1;
                if(j == limit)
                    ans = (ans + dfs(i-1, max_flag, next)) % MOD;
                else
                    ans = (ans + dfs(i-1, 2, next)) % MOD;
            }
        }
        return dp[i][max_flag][prev+1] = ans;
    }
    
    int countSteppingNumbers(string low, string high) {
        low = decrementString(low);
        maximums = {high, low};
        dp.resize(high.size() + 1, vector<vector<int>>(3, vector<int>(12, -1)));
        return (dfs(high.size(), 0, -1) - dfs(low.size(), 1, -1) + MOD) % MOD;
    }
};