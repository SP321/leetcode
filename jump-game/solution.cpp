class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n=nums.size();
        int reach=0;
        for(int i=0;i<n;i++){
            if(i>reach)
                return 0;
            reach=max(reach,i+nums[i]);
        }
        return 1;
    }
};