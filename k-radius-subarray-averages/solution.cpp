class Solution {
public:
    vector<int> getAverages(vector<int>& nums, int k) {
        int m = 2 * k + 1;
        int n = nums.size();
        vector<int> ans(n, -1);
        
        long long window_sum = 0;
        for (int i = 0; i < n; ++i) {
            window_sum += nums[i];
            if (i >= m) {
                window_sum -= nums[i - m];
            }
            if (i >= m - 1) {
                ans[i - k] = window_sum / m;
            }
        }

        return ans;
    }
};