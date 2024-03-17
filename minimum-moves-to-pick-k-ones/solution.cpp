class Solution {
public:
    long long minimumMoves(vector<int>& nums, int k, int maxChanges) {
        vector<long long> pre={0};
        for (int i = 0; i < nums.size(); ++i)
            if (nums[i])
                pre.push_back(pre.back()+i);
        int n = pre.size()-1;
        int min_sz = max(0, k - maxChanges);
        int max_sz = min(min_sz + 3, min(n,k));
        long long ans = 1e11;
        for (int sz = min_sz; sz <= max_sz; ++sz) {
            for (int i = 0; i <= n - sz; ++i) {
                int j = i + sz;
                int half = sz / 2;
                long long cur = (k - sz) * 2ll + (pre[j] - pre[j - half]) -
                          (pre[i + half] - pre[i]);
                ans = min(ans, cur);
            }
        }
        return ans;
    }
};