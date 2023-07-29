class Solution {
public:
    vector<vector<int>>dp;
    vector<int> x;
    int dfs(int i,int j){
        if(i>j)
            return 0;
        if(dp[i][j]!=INT_MAX)
            return dp[i][j];
        dp[i][j]=max(x[i] - dfs(i + 1, j),x[j] - dfs(i, j - 1));
        return dp[i][j];
    }
    bool PredictTheWinner(vector<int>& nums) {
        int n=nums.size();
        x=nums;
        dp.resize(n,vector<int>(n,INT_MAX));
        return dfs(0, n - 1) >= 0;
    }
};