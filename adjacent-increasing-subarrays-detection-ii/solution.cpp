class Solution {
public:
    int maxIncreasingSubarrays(vector<int>& nums) {
        int n = nums.size();
        int i = 0, prev = 0, ans = 0;
        int cur=0;
        for (int j = 0; j < n; ++j) {
            if (j != 0 && nums[j] <= nums[j - 1]) {
                i = j;
                prev = cur;
            }
            cur = j - i + 1;
            ans = max(ans, cur / 2);
            ans = max(ans, min(prev, cur));
        }
        
        return ans;
    }
};