class Solution {
public:
    int findMin(vector<int>& nums) {
        int x=nums[0];
        int i=0;
        int j=nums.size()-1;
        int ans=i;
        while(i<=j){
            const int m=i+(j-i)/2;
            if(nums[m]>=x)
                i=m+1;
            else{
                ans=m;
                j=m-1;
            }
        }
        return nums[ans];
            
    }
};