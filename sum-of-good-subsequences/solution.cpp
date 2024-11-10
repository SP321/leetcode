
int MOD = 1000000007;
class Solution {
public:
    int sumOfGoodSubsequences(vector<int>& nums) {
        unordered_map<int, int> c;
        unordered_map<int, long long> dp;

        for (int x : nums) {
            int cnt = c[x - 1] + c[x + 1] + 1;
            dp[x] += (dp[x - 1] + dp[x + 1] + 1ll*x * cnt);
            cnt %= MOD;
            c[x] += cnt;
            dp[x] %= MOD;
            c[x] %= MOD;
        }

        int ans = 0;
        for (const auto& entry : dp) {
            ans = (ans + entry.second) % MOD;
        }

        return ans;
    }
};