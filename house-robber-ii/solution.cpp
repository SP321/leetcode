
class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.empty()) return 0;
        if (nums.size() == 1) return nums[0];

        return max(
            robRange(nums, 1, nums.size() - 1),
            robRange(nums, 0, nums.size() - 2)
        );
    }

    map<int, int> memo;
    
    int robRange(const vector<int>& nums, int start, int end) {
        memo.clear();
        return dp(nums, start, end);
    }
    
    int dp(const vector<int>& nums, int i, int end) {
        if (i > end) return 0;
        if (memo.find(i) != memo.end()) return memo[i];
        
        int result = max(dp(nums, i + 1, end),
                         nums[i] + dp(nums, i + 2, end));
        memo[i] = result;
        return result;
    }
};