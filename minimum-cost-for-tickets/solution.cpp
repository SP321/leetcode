class Solution {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        int n=days.size();
        vector<int>dp(days[n-1]+1);
        int p=0;
        for(int i=1;i<=days[n-1];i++){
            if(i==days[p]){
                p++;
                dp[i]=min(
                    dp[max(0,i-1)]+costs[0],
                    min(
                        dp[max(0,i-7)]+costs[1],
                        dp[max(0,i-30)]+costs[2]
                    )
                );
            }
            else
                dp[i]=dp[i-1];
        }
        return dp[dp.size()-1];
    }
};