class Solution {
public:
    int minTaps(int n, vector<int>& ranges) {
        vector<pair<int, int>> a;
        for (int i = 0; i < ranges.size(); ++i) {
            a.emplace_back(i - ranges[i], i + ranges[i]);
        }
        
        sort(a.begin(), a.end(), [](const pair<int, int>& x, const pair<int, int>& y) {
            return x.first < y.first || (x.first == y.first && x.second > y.second);
        });
        
        int ans = 0;
        int i = 0;
        int watered = 0;
        
        while (watered < n) {
            int can_water_to = watered;
            while (i < a.size() && a[i].first <= watered) {
                can_water_to = max(can_water_to, a[i].second);
                ++i;
            }
            if (can_water_to == watered) {
                return -1;
            }
            watered = can_water_to;
            ++ans;
        }
        
        return ans;
    }
};