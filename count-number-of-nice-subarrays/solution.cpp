class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        int count = 0, ans = 0;
        unordered_map<int, int> dp;
        dp[0] = 1;

        for (int &num : nums) {
            if (num % 2 == 1) {
                count++;
            }
            if (dp.find(count - k) != dp.end()) {
                ans += dp[count - k];
            }
            dp[count]++;
        }

        return ans;
    }
};