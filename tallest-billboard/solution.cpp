class Solution {
public:
    int tallestBillboard(vector<int>& rods) {
        map<int, int> dp;
        dp[0] = 0;
        for (int rod : rods) {
            map<int, int> curr(dp);
            for (auto& item : curr) {
                int diff = item.first;
                int max_y = item.second;
                dp[diff + rod] = max(dp[diff + rod], max_y);
                dp[abs(diff - rod)] = max(dp[abs(diff - rod)], max_y + min(diff, rod));
            }
        }
        return dp[0];
    }
};