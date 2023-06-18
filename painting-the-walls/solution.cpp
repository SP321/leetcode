class Solution {
public:
    vector<vector<int>>dp;
    vector<int>cost;
    vector<int>time;
    int n;
    int paintWalls(vector<int>& cost, vector<int>& time) {
        n=cost.size();
        this->cost=cost;
        this->time=time;
        dp.resize(n,vector<int>(n+1,-1));
        return dfs(0, n);
    }
    int dfs(int i, int j) {
        if (j < 1)
            return 0;
        if (i == cost.size())
            return 1e6*500;
        if(dp[i][j]!=-1)
            return dp[i][j];
        int include = cost[i] + dfs(i + 1, j - time[i] - 1);
        int exclude = dfs(i + 1, j);
        return dp[i][j]=min(include, exclude);
    }
};