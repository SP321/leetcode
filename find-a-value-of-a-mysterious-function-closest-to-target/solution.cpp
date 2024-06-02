class Solution {
public:
    int closestToTarget(vector<int>& arr, int target) {
        int ans = INT_MAX;
        unordered_set<int> dp0;

        for (int x : arr) {
            unordered_set<int> dp1;
            dp0.insert(x);
            for (int y : dp0) {
                dp1.insert(x & y);
                ans = min(ans, abs((x & y) - target));
            }
            dp0 = dp1;
        }

        return ans;
    }
};