class Solution {
    int n;
    vector<vector<vector<int>>>dp;
    vector<int>a;
public:
    int stoneGameII(vector<int>& piles) {
        a=piles;
        n=a.size();
        dp.resize(2,vector<vector<int>>(n,vector<int>(n*2,-1)));
        return dfs(1,0,1);
    }
    int dfs(int alice,int i,int m){
        if(i==n)
            return 0;
        if(dp[alice][i][m]!=-1)
            return dp[alice][i][m];
        int ma=0,mi=1e9;
        int cur_stones=0;
        for(int x=1;x<=2*m;x++){
            int j=i+x-1;
            if(j>=n)
                break;
            cur_stones+=a[j];
            int nextmove=dfs(!alice,j+1,max(m,x));
            mi=min(mi,nextmove);
            ma=max(ma,cur_stones+nextmove);
        }
        if(alice)
            dp[alice][i][m]=ma;
        else
            dp[alice][i][m]=mi;
        return dp[alice][i][m];
    }
};