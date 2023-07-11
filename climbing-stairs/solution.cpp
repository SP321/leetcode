class Solution {
public:
    map<int, int> dp;
    int climbStairs(int n) {
        if (n <= 2) {
            return n;
        }
        if (dp.find(n) == dp.end()) {
            dp[n] = climbStairs(n - 1) + climbStairs(n - 2);
        }
        return dp[n];
    }
};