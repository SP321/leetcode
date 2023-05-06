class Solution {
public:
    int search(vector<int>& nums, int target) {
        int x=nums[0];
        int i=0;
        int j=nums.size()-1;
        while(i<=j){
            const int m=i+(j-i)/2;
            if(target==nums[m])
                return m;
            if(nums[m]<x){
                if(target<nums[m] ||target >=x)
                    j=m-1;
                else
                    i=m+1;
            }
            else{
                if(target<nums[m] && target >=x)
                    j=m-1;
                else
                    i=m+1;
            }
        }
        return -1;
    }
};