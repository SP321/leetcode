class Solution {
public:
    int countGoodStrings(int low, int high, int zero, int one) {
        vector<int>dp(high+1,-1);
        dp[0]=1;
        int md=1e9+7;
        for(int i=0;i<high;i++){
            if(dp[i]>=0){
                if(i+zero<=high){
                    dp[i+zero]=max(dp[i+zero],0);
                    dp[i+zero]+=dp[i];
                    dp[i+zero]%=md;
                }
                if(i+one<=high){
                    dp[i+one]=max(dp[i+one],0);
                    dp[i+one]+=dp[i];
                    dp[i+one]%=md;
                }
            }
        }
        int ans=0;
        for(int i=low;i<=high;i++){
            ans+=max(dp[i],0);
            ans%=md;
        }
        return ans;
    }
};