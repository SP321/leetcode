class Solution {
public:
    int ans = 0;
    int subsetXORSum(vector<int>& nums) {
        dfs(nums, 0, 0);
        return ans;
    }
    void dfs(vector<int>& nums, int i, int x) {
        if (i == nums.size()) {
            ans += x;
            return;
        }
        dfs(nums, i + 1, x ^ nums[i]);
        dfs(nums, i + 1, x);
    }
};