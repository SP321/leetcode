class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int m=prices[0];
        int ans=0;
        for(auto &i:prices){
            m=min(m,i);
            ans=max(ans,i-m);
        }
        return ans;
    }
};