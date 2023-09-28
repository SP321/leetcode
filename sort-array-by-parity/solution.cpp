class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        int j=nums.size()-1;
        for(int i=0;i<j;i++){
            while(i<j and nums[j]%2)
                j--;
            if(nums[i]%2)
                swap(nums[i],nums[j]);
        }
        return nums;
    }
};