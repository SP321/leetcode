
class Solution {
public:
    int maximumCostSubstring(string s, string chars, vector<int>& vals) {
        vector<int> x;
        const int n=s.size();
        for(int i=0;i<n;i++){
            int score=s[i]-'a'+1;
            for(int j=0;j<chars.size();j++){
                if(chars[j]==s[i])
                    score=vals[j];
            }
            x.push_back(score);
        }
        
        vector<int>dp(n+1,0);
        dp[0]=0;
        int ans=0;
        for (int i=1;i<=n;i++){
            dp[i]=max(dp[i-1]+x[i-1],x[i-1]);
            ans=max(ans,dp[i]);
        }
        return ans;
    }
};