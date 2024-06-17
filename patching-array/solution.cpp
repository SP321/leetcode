class Solution {
public:
    int minPatches(vector<int>& nums, int n) {
        long long reach = 0;
        int ans = 0, idx = 0;

        while (reach < n) {
            if (idx < nums.size() && nums[idx] <= reach + 1) {
                reach += nums[idx];
                idx++;
            } else {
                ans++;
                reach = 2 * reach + 1;
            }
        }
        return ans;
    }
};