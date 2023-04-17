class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int>c;
        int n=nums.size();
        for(int i=0;i<n;i++)
            c[nums[i]]=i;
        for(int i=0;i<n;i++)
            if(c[target-nums[i]] && i!=c[target-nums[i]])
                return {i,c[target-nums[i]]};
        return {};
    }
};