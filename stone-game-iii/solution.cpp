class Solution {
public:
    int n;
    vector<int>a;
    vector<int>dp;
    string stoneGameIII(vector<int>& stoneValue) {
        a=stoneValue;
        n=a.size();
        dp.resize(n+1,-1);
        int x=dfs(0);
        cout<<x<<endl;
        if(x>0)
            return "Alice";
        else if(x<0)
            return "Bob";
        return "Tie";
    }
    int dfs(int i){
        if (i==n)
            return 0;
        if(dp[i]!=-1)
            return dp[i];
        int sc=0;
        dp[i]=INT_MIN;
        for(int j=i;j<min(i+3,n);j++){
            sc+=a[j];
            dp[i]=max(dp[i],sc-dfs(j+1));
        }
        return dp[i];
    }
};