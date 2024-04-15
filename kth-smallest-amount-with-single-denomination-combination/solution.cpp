class Solution {
public:
    long long findKthSmallest(vector<int>& coins, int k) {
        unordered_map<long long, int> c;
        int n = coins.size();
        for (int mask = 1; mask < (1 << n); mask++) {
            long long x = 1;
            for (int i = 0; i < n; i++) {
                if ((1 << i) & mask) {
                    x = lcm(x, coins[i]);
                }
            }
            if (__builtin_popcount(mask) % 2) {
                c[x] += 1;
            } else {
                c[x] -= 1;
            }
        }

        auto check = [&](long long m) {
            long long pos = 0;
            for (auto& p : c) {
                pos += (m / p.first) * p.second;
            }
            return pos >= k;
        };

        long long l = 1, r = *min_element(coins.begin(), coins.end()) * (long long)k;
        while (l < r) {
            long long m = l + (r - l) / 2;
            if (check(m)) {
                r = m;
            } else {
                l = m + 1;
            }
        }
        return l;
    }
};