class Solution {
public:
    int minimumDifference(vector<int>& nums, int k) {
        int ans = INT_MAX;
        unordered_set<int> dp0;

        for (int x : nums) {
            unordered_set<int> dp1;
            dp0.insert(x);
            for (int y : dp0) {
                dp1.insert(x & y);
                ans = min(ans, abs((x & y) - k));
            }
            dp0 = dp1;
        }

        return ans;
    }
};