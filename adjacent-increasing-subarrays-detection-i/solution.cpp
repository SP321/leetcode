class Solution {
public:
    bool hasIncreasingSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        int i = 0, prev = 0, cur=0;
        for (int j = 0; j < n; ++j) {
            if (j != 0 && nums[j] <= nums[j - 1]) {
                i = j;
                prev = cur;
            }
            cur = j - i + 1;
            if (cur==k*2 or cur == k && prev >= k) {
                return true;
            }
        }
        return false;
    }
};