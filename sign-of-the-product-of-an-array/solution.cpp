class Solution {
public:
    int arraySign(vector<int>& nums) {
        std::ios::sync_with_stdio(false);
        int nc=0;
        int n=nums.size();
        for(int i=0;i<n;i++){
            if(nums[i]<0)
                nc=!nc;
            else if(nums[i]==0)
                return 0;
        }
        if(nc)
            return -1;
        return 1;
    }
};