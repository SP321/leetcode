class Solution {
public:
    map<int,vector<int>>x;
    Solution(vector<int>& nums) {
        for(int i=0;i<nums.size();i++)
            x[nums[i]].push_back(i);
    }
    
    int pick(int target) {
        auto y = x[target].begin();
        advance(y, rand() % x[target].size());
        return *y;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * int param_1 = obj->pick(target);
 */