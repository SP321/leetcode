class Solution {
public:
    int countDays(int days, vector<vector<int>>& meetings) {
        meetings.push_back({0, 0});
        meetings.push_back({days + 1, days + 1});
        sort(meetings.begin(), meetings.end());
        int ans = 0;
        int y = 0;
        for (const auto& cur : meetings) {
            int x = cur[0], yy = cur[1];
            ans += max(0, x - y - 1);
            y = max(y, yy);
        }
        return ans;
    }
};