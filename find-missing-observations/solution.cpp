class Solution {
public:
    vector<int> missingRolls(vector<int>& rolls, int mean, int n) {
        int m = rolls.size();
        int x = accumulate(rolls.begin(), rolls.end(), 0);
        int total = mean * (n + m);
        int y = total - x;
        
        int q = y / n;
        int r = y % n;
        vector<int> ans(n, 0);

        for (int i = 0; i < n; ++i) {
            ans[i] += q;
            if (i < r) {
                ans[i] += 1;
            }
            if (ans[i] < 1 || ans[i] > 6) {
                return {};
            }
        }
        
        return ans;
    }
};