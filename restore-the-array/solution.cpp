class Solution {
public:
    string a;
    int n;
    int b;
    vector<int>dp;
    int ans;
    int md=1e9+7;
    int numberOfArrays(string s, int k) {
        a=s;
        n=a.size();
        b=k;
        dp.resize(n+1,-1);
        int ans=solve(0);
        return max(0,dp[0]);
    }
    int solve(int i){
        if(dp[i]!=-1)
            return dp[i];
        if(i>=n){
            dp[i]= 1;
            return 1;
        }
        long long num=0;
        int j=i;
        if(a[i]=='0'){
            dp[i]=0;
            return 0;
        }
        dp[i]=0;
        for(;j<n;j++){
            num=num*10+a[j]-'0';
            if(num>b)
                break;
            int x=solve(j+1);
            if(x)
                dp[i]+=x;
                dp[i]%=md;
        }
        return dp[i];
    }
};