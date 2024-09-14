class Solution {
public:
    int maxEnvelopes(vector<vector<int>>& envelopes) {
        sort(envelopes.begin(), envelopes.end(), [](auto& a,auto& b) {
            if (a[0] == b[0]) {
                return a[1] > b[1];
            }
            return a[0] < b[0];
        });
        vector<int> ans;
        for (const auto& p : envelopes) {
            int y=p[1];
            auto it = lower_bound(ans.begin(), ans.end(), y);
            if (it == ans.end()) {
                ans.push_back(y);
            } else {
                *it = y;
            }
        }
        return ans.size();
    }
};