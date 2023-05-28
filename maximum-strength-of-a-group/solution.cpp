class Solution {
public:
    long long maxStrength(vector<int>& nums) {
        int n = nums.size();
        long long ans = LLONG_MIN;

        for (int i = 1; i < (1 << n); i++) {
            long long product = 1;
            for (int j = 0; j < n; j++) {
                if ((i & (1 << j)) != 0) {
                    product *= nums[j];
                }
            }
            ans = max(ans,product);
        }

        return ans;
    }
};