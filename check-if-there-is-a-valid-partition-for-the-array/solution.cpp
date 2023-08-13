class Solution {
public:
    bool validPartition(vector<int>& nums) {
        this->nums = nums;
        dp.resize(nums.size(),-1);
        return dfs(0);
    }
    vector<int>nums;
    vector<int>dp;
    bool dfs(int i) {
        if(i == nums.size()) {
            return true;
        }
        if(dp[i]!=-1) {
            return dp[i];
        }
        bool ans = false;

        if(i + 1 < dp.size() && nums[i] == nums[i + 1]) {
            ans |= dfs(i + 2);
        }
        if(i + 2 < nums.size() && nums[i] == nums[i + 1] && nums[i] == nums[i + 2]) {
            ans |= dfs(i + 3);
        }
        if(i + 2 < nums.size() && nums[i + 2] - nums[i + 1] == 1 && nums[i + 1] - nums[i] == 1) {
            ans |= dfs(i + 3);
        }
        dp[i] = ans;
        return ans;
    }
};
