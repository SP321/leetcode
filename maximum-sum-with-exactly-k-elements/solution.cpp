class Solution {
public:
    int maximizeSum(vector<int>& nums, int k) {
        int ma=0;
        for(auto &i:nums)
            ma=max(ma,i);
        int ans=0;
        while(k--)
            ans+=ma++;
        return ans;
    }
};