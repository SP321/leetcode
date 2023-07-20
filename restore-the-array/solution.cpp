class Solution {
public:
    string s;
    int k;
    vector<int> dp;
    int md = 1000000007;
    int n;
    
    int numberOfArrays(string s, int k) {
        this->s = s;
        this->k = k;
        n = s.size();
        dp.resize(n+1, -1);
        return dfs(0);
    }

    int dfs(int i) {
        if (i == n)
            return 1;
        if (s[i] == '0') 
            return 0;
        if (dp[i] != -1)
            return dp[i];

        long long x = 0;
        int ways = 0;
        for (int j = i; j < n; j++) {
            x = (x * 10) + s[j] - '0';
            if (x < 1 || x > k)
                break;
            ways = (ways + dfs(j + 1)) % md;
        }
        dp[i] = ways;
        return dp[i];
    }
};