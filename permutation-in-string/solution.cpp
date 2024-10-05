class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        vector<int> a(27, 0), b(27, 0);
        for (char i : s1) {
            a[i % 32]++;
        }
        for (int i = 0; i < s2.size(); i++) {
            b[s2[i] % 32]++;
            if (i >= s1.size()) {
                b[s2[i - s1.size()] % 32]--;
            }
            if (a == b) {
                return true;
            }
        }
        return false;
    }
};
static const int _ = []() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    return 0;
}();