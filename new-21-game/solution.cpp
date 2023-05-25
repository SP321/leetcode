class Solution {
public:
    double new21Game(int n, int k, int maxPts) {
        if (k == 0 || k + maxPts <= n) {
            return 1.0;
        }
        double window = 0.0;
        for (int i = k; i < k + maxPts; ++i) {
            window += (i <= n) ? 1 : 0;
        }
        vector<double> dp(k + maxPts + 1, 0);
        for (int i = k - 1; i >= 0; --i) {
            dp[i] = window / maxPts;
            double rem = 0.0;
            if (i + maxPts <= n) {
                if (dp[i + maxPts] == 0) {
                    dp[i + maxPts] = 1;
                }
                rem = dp[i + maxPts];
            }
            window = window + dp[i] - rem;
        }
        return dp[0];
    }
};