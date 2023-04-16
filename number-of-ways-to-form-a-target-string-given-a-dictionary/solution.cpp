class Solution {
public:
    const int md = 1e9+7;
    vector<string> a;
    string t;
    int n, m, nn;
    vector<vector<int>> dp;
    vector<vector<int>> c;

    int numWays(vector<string>& words, string target) {
        a = words;
        t = target;
        n = t.size();
        m = a[0].size();
        nn = a.size();

        dp.resize(n+1, vector<int>(m+1, 0));
        c.resize(m, vector<int>(26));

        for (int i = 0; i < nn; i++)
            for (int j = 0; j < m; j++)
                c[j][words[i][j] - 'a']++;

        for(int j=m;j>=0;j--)
            dp[n][j]=1;
            
        for(int i=n-1;i>=0;i--)
            for(int j=m-1;j>=0;j--){
                dp[i][j]= ((long long)dp[i+1][j+1]*c[j][t[i]-'a']%md)%md + dp[i][j+1];
                dp[i][j]%=md;
            }
        return dp[0][0];    
    }
};