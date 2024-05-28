class Solution {
public:
    int equalSubstring(string s, string t, int maxCost) {
        int i=0,cost=0,ans=0;
        for(int j=0;j<s.size();j++){
            cost+=abs(s[j]-t[j]);
            while (i<j and cost>maxCost){
                cost-=abs(s[i]-t[i]);
                i+=1;
            }
            if(cost<=maxCost)
                ans=max(ans,j-i+1);
        }
        return ans;
    }
};