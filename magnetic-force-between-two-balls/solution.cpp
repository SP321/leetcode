
auto init = []() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    return 'c';
}();
class Solution {
public:
    int maxDistance(vector<int>& position, int m) {
        sort(position.begin(), position.end());
        
        auto check = [&](int k) {
            int c = m;
            int ban = -1;
            for (int x : position) {
                if (x > ban) {
                    ban = x + k - 1;
                    c--;
                    if (c == 0) break;
                }
            }
            return c > 0;
        };
        
        int left = 1, right = position[position.size()-1];
        while (left < right) {
            int mid = left + (right - left + 1) / 2;
            if (check(mid)) {
                right = mid - 1;
            } else {
                left = mid;
            }
        }
        
        return left;
    }
};