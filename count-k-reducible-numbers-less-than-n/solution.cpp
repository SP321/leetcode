const int MOD = 1e9 + 7;
class Solution {
public:
    string s;
    vector<string> MX;
    int n;
    int k;

    unordered_map<int, int> dp1_cache;

    int dp1(int x) {
        if (x == 1) return 0;
        auto it = dp1_cache.find(x);
        if (it != dp1_cache.end()) return it->second;
        int res = dp1(__builtin_popcount(x)) + 1;
        dp1_cache[x] = res;
        return res;
    }

    unordered_map<long long, int> dp_cache;

    int dp(int i, int mx_, int cnt) {
        long long key = 1ll*i+1ll*cnt*800+1ll*800*800*mx_ ;
        auto it = dp_cache.find(key);
        if (it != dp_cache.end()) return it->second;

        const string& mx = MX[mx_];
        if (i == n) {
            int res = (cnt > 0 && dp1(cnt) < k) ? 1 : 0;
            dp_cache[key] = res;
            return res;
        }

        int cur_max = mx[i] - '0';
        int ans = 0;
        for (int dig = 0; dig <= cur_max; ++dig) {
            int next_mx_ = (mx_ != 0 || dig != cur_max) ? 1 : 0;
            ans = (ans + dp(i + 1, next_mx_, cnt + dig)) % MOD;
        }

        dp_cache[key] = ans;
        return ans;
    }

    int countKReducibleNumbers(string s, int k) {
        this->s = s;
        this->k = k;
        this->n = s.size();
        for (int i = n - 1; i >= 0; --i) {
            if (s[i] == '0') {
                s[i] = '1';
            } else {
                s[i] = '0';
                break;
            }
        }
        MX = {s, string(n, '1')};
        return dp(0, 0, 0);
    }
};