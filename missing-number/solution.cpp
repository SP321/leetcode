class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int ans=n*(n+1)/2;
        for(int &i:nums)
            ans-=i;
        return ans;
    }
};