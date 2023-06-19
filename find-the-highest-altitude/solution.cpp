class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int x=0,ans=0;
        for(int &i:gain){
            x+=i;
            ans=max(ans,x);
        }
        return ans;
    }
};