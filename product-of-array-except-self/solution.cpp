class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int>ans(nums.size());
        int x=1;
        for(int i=0;i<nums.size();i++){
            ans[i]=x;
            x*=nums[i];
        }
        x=1;
        for(int i=nums.size()-1;i>=0;i--){
            ans[i]*=x;
            x*=nums[i];
        }
        return ans;
    }
};