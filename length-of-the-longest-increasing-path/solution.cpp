class Solution {
public:
    int lis(vector<vector<int>>& arr) {
        sort(arr.begin(), arr.end(), [](const vector<int>& a, const vector<int>& b) {
            if (a[0] == b[0])
                return a[1] > b[1];
            return a[0] < b[0];
        });
        vector<int> res;
        for (const auto& coord : arr) {
            int y = coord[1];
            auto it = lower_bound(res.begin(), res.end(), y);
            if (it == res.end()) {
                res.push_back(y);
            } else {
                *it = y;
            }
        }
        return res.size();
    }

    int maxPathLength(vector<vector<int>>& coordinates, int k) {
        int mx = coordinates[k][0];
        int my = coordinates[k][1];
        
        sort(coordinates.begin(), coordinates.end());

        vector<vector<int>> left, right;
        for (const auto& point : coordinates) {
            int x = point[0], y = point[1];
            if (x < mx && y < my) {
                left.push_back({x, y});
            } else if (x > mx && y > my) {
                right.push_back({x, y});
            }
        }

        return 1 + lis(left) + lis(right);
    }
};