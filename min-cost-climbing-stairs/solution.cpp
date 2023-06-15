class Solution {
public:
    vector<int>dp;
    vector<int>a;
    int n;
    int dfs(int i) {
        if(i >= n)
            return 0;
        if (dp[i]!=-1)
            return dp[i];
        return dp[i] = a[i] + min(dfs(i+1), dfs(i+2));
    }

    int minCostClimbingStairs(vector<int>& cost) {
        n=cost.size();
        dp.resize(n,-1);
        a=cost;
        return min(dfs(0), dfs(1));
    }
};