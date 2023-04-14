class Solution {
public:
    int longestPalindromeSubseq(string s) {
        int n=s.size();
        vector<vector<int>>dp(n+1,vector<int>(n+1,0));
        dp[0][0]=0;
        for(int i=1;i<=n;i++)
            for(int j=1;j<=n;j++)
                if(s[i-1]==s[n-j])
                    dp[i][j]=1;
        
        for(int i=1;i<=n;i++)
            for(int j=1;j<=n;j++)
                dp[i][j]=max(dp[i][j]+dp[i-1][j-1],max(dp[i-1][j] ,dp[i][j-1]));

        // for(int i=0;i<=n;i++){
        //     for(int j=0;j<=n;j++)
        //         cout<<dp[i][j]<<" ";
        //     cout<<endl;
        // }
        return dp[n][n];
    }
};