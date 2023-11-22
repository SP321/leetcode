class Solution {
public:
    int maxAscendingSum(vector<int>& nums) {
        int s=0;
        int ans=0;
        for(int i=0;i<nums.size();i++){
            if(i==0 or nums[i]>nums[i-1])
                s+=nums[i];
            else
                s=nums[i];
            ans=max(ans,s);
        }
        return ans;
    }
};