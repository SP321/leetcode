class Solution {
public:
    long long mostPoints(vector<vector<int>>& questions) {
        int n=questions.size();
        vector<long long>dp(n+1,0);
        for(int i=0;i<n;i++){
            int a=min(n,i+questions[i][1]+1);
            dp[a]=max(dp[a],dp[i]+questions[i][0]);
            dp[i+1]=max(dp[i],dp[i+1]);
        }
        return dp[n];
    }
};