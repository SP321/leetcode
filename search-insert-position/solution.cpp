class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int l=0;
        int h=nums.size();
        int m=(l+h)/2;
        while(l<h){
            if(nums[m]<target)
                l=m+1;
            else if(nums[m]>target)
                h=m;
            else
                return m;
            m=(l+h)/2;
        }
        return m;
    }
};