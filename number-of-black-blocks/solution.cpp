class Solution {
public:
    vector<long long> countBlackBlocks(int m, int n, vector<vector<int>>& coordinates) {
        map<pair<int, int>, long long> d;
        for (auto& i : coordinates) {
            int x = i[0];
            int y = i[1];
            for (int dx = 0; dx <= 1; dx++) {
                for (int dy = 0; dy <= 1; dy++) {
                    if (0 <= x - dx && x - dx < m - 1 && 0 <= y - dy && y - dy < n - 1) {
                        pair<int, int> block(x - dx, y - dy);
                        d[block]++;
                    }
                }
            }
        }
        
        vector<long long> ans(5, 0);
        long long nonzero=0;
        for (auto& [key,count] : d) {
            ans[count]++;
            nonzero++;
        }
        ans[0] = 1ll*(m - 1) * (n - 1) - nonzero;
        return ans;
    }
};