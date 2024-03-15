class Solution {
public:
    int hIndex(vector<int>& citations) {
        int ans=0;
        sort(citations.begin(),citations.end());
        int n=citations.size();
        for(auto &x:citations){
            ans=max(ans,min(x,n));
            n-=1;
        }
        return ans;
    }
};