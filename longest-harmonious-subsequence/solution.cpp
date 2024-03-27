class Solution {
public:
    int findLHS(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int ans=0;
        int i=0;
        for(int j=0;j<nums.size();j++){
            while(nums[j]-nums[i]>1)
                i+=1;
            if(nums[j]!=nums[i])
                ans=max(ans,j-i+1);
        }
        return ans;
    }
};