class Solution {
public:
    long long maximumSum(vector<int>& A) {
        unordered_map<int, long long> count;
        int n = A.size();

        for (int i = 0; i < n; ++i) {
            int x = i + 1;
            int v = 2;
            while (v * v <= x) {
                while (x % (v * v) == 0) {
                    x /= v * v;
                }
                v++;
            }
            count[x] += A[i];
        }

        long long ans = 0;
        for (auto& p : count) {
            ans = max(ans, p.second);
        }
        return ans;
    }
};
