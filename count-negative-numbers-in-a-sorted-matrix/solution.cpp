class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int ans = 0;
        int cur_r = grid[0].size() - 1;
        for (const auto& row : grid) {
            int l = 0;
            int r = cur_r;
            while (l <= r) {
                int mid = (l + r) / 2;
                if (row[mid] < 0) {
                    r = mid - 1;
                    cur_r = r;
                } else {
                    l = mid + 1;
                }
            }
            ans += grid[0].size() - l;
        }
        return ans;
    }
};
