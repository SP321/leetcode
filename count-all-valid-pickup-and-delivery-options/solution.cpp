class Solution {
public:
    vector<vector<int>> dp;
    int md = 1e9 + 7;

    int countOrders(int n) {
        dp.resize(n + 1, vector<int>(n + 1, -1));
        return dfs(n, n);
    }
    int dfs(int pickup, int delivery) {
        if (pickup == 0 && delivery == 0) return 1;
        if (dp[pickup][delivery] != -1) return dp[pickup][delivery];

        int ans = 0;
        if (pickup > 0)
            ans = (ans + 1ll*dfs(pickup - 1, delivery) * pickup) % md;
        if (pickup < delivery) 
            ans = (ans + 1ll*dfs(pickup, delivery - 1) * (delivery - pickup)) % md;
        dp[pickup][delivery] = ans%md;
        return dp[pickup][delivery];
    }
};