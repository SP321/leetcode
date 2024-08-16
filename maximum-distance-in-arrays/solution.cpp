class Solution {
public:
    int maxDistance(vector<vector<int>>& arrays) {
        int mi = arrays[0][0];
        int mx = arrays[0].back();
        int ans = 0;

        for (int i = 1; i < arrays.size(); ++i) {
            int a = arrays[i][0];
            int b = arrays[i].back();
            ans = max(ans, abs(a - mi));
            ans = max(ans, abs(a - mx));
            ans = max(ans, abs(b - mi));
            ans = max(ans, abs(b - mx));
            mi = min(mi, a);
            mx = max(mx, b);
        }

        return ans;
    }
};
