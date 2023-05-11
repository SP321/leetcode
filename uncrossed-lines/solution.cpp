class Solution {
public:
    int n;
    int m;
    vector<int>a,b;
    vector<vector<int>>dp;
    int solve(int i,int j){
        if(i>=n|| j>=m)
            return 0;
        if(dp[i][j]!=-1)
            return dp[i][j];
        dp[i][j]=max(solve(i,j+1),solve(i+1,j));
        if(a[i]==b[j])
            dp[i][j]=max(dp[i][j],1+solve(i+1,j+1));
        return dp[i][j];
    }
    int maxUncrossedLines(vector<int>& nums1, vector<int>& nums2) {
        n=nums1.size();
        m=nums2.size();
        a=nums1;
        b=nums2;
        dp.resize(n,vector<int>(m,-1));
        return solve(0,0);
    }
};