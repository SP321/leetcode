class Solution {
public:
    bool isMatch(string s, string p) {
        const int n=p.size();
        const int m=s.size();
        vector<vector<int>> dp(n+1,vector<int>(m+1,0));
        dp[0][0]=1;
        for(int i=1;i<=n;i++)
            if(p[i-1]=='*')
                dp[i][0]=dp[i-2][0];
        for(int i=1;i<=n;i++){
            for(int j=1;j<=m;j++){
                if(p[i-1]==s[j-1] || p[i-1] =='.'){
                    dp[i][j]=dp[i-1][j-1];
                }
                if(p[i-1]=='*'){
                    dp[i][j]=dp[i-2][j]|dp[i-1][j];
                    if(p[i-2]==s[j-1]||p[i-2]=='.')
                        dp[i][j]=dp[i][j]|dp[i][j-1];
                }
            }
        }
        return (bool)dp[n][m];
    }
};