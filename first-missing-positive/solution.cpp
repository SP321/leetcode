class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n=nums.size();
        vector<int>c(n+2);
        for(int i=0;i<n;i++){
            if(nums[i]>0 &&nums[i]<=n)
                c[nums[i]]=1;
        }
        for(int i=1;i<=n+1;i++)
            if(!c[i])
                return i;
        return -1;
    }
};