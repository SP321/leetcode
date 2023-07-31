class Solution {
public:
    string s1,s2;
    int n,m;
    vector<vector<int>>dp;
    int minimumDeleteSum(string s1, string s2) {
        this->s1=s1;
        this->s2=s2;
        n=s1.size();
        m=s2.size();
        int sum=0;
        for(char &i:s1)
            sum+=i;
        for(char &i:s2)
            sum+=i;
        dp.resize(n,vector<int>(m,-1));
        return sum-dfs(0,0);
        
    }
    int dfs(int i,int j){
        if (i==n or j==m)
            return 0;
        if(dp[i][j]!=-1)
            return dp[i][j];
        if(s1[i]==s2[j])
            return dp[i][j]=dfs(i+1,j+1)+s1[i]*2;
        return dp[i][j]=max(dfs(i+1,j),dfs(i,j+1));
    }
};