class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n=nums.size();
        for(int i=0;i<n;i++){
            if(nums[i]<=0 or nums[i]>n)
                nums[i]=n+1;
        }
        for(int i=0;i<n;i++){
            int cur=abs(nums[i]);
            if(cur==n+1)
                continue;
            if(nums[cur-1]>0)
                nums[cur-1]=-nums[cur-1];
        }
        for(int i=0;i<n;i++){
            if(nums[i]>0)
                return i+1;
        }
        return n+1;
    }
};