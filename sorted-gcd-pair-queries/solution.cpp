class Solution {
public:
    vector<int> gcdValues(vector<int>& nums, vector<long long>& queries) {
        int mx = -1;
        unordered_map<int, int> freq;
        for (auto &x: nums) {
            freq[x]+=1;
            mx=max(mx,x);
        }
        
        vector<long long> dp(mx + 1, 0);

        for (int g = mx; g >= 1; --g) {
            long long c = freq[g];
            for (int m = 2 * g; m <= mx; m += g) {
                c += freq[m];
                dp[g] -= dp[m];
            }
            dp[g] += c * (c - 1) / 2;
        }

        partial_sum(dp.begin(), dp.end(), dp.begin());

        vector<int> ans;
        for (long long x : queries) {
            auto pos = lower_bound(dp.begin(), dp.end(), x + 1) - dp.begin();
            ans.push_back(pos);
        }

        return ans;
    }
};