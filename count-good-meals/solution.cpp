class Solution {
public:
    int countPairs(const vector<int>& deliciousness) {
        unordered_map<int, int> c;
        int ans = 0;
        const int MOD = 1e9 + 7;
        vector<int> powersOfTwo(22);
        for (int i = 0; i <= 21; ++i) {
            powersOfTwo[i] = (1 << i);
        }

        for (int x : deliciousness) {
            for (int power : powersOfTwo) {
                if (c.find(power - x) != c.end()) {
                    ans += c[power - x];
                    ans %= MOD;
                }
            }
            c[x]++;
        }

        return ans;
    }
};
