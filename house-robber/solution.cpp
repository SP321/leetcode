class Solution {
public:
    int rob(vector<int>& nums) {
        int n=nums.size();
        vector<int>dp(n+2,0);
        for(int i=0;i<n;i++)
            dp[i+2]=max(dp[i+1],dp[i]+nums[i]);
        return max(dp[n],dp[n+1]);
    }
};