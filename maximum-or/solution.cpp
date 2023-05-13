class Solution {
public:
    long long maximumOr(vector<int>& nums, int k) {
        int or_ = 0;
        int or_multiple = 0;
        
        for (int i : nums) {
            or_multiple |= i & or_;
            or_ |= i;
        }
        long long ans = 0;
        for (long long i : nums) {
            long long x = or_ & ~(i);
            x |= or_multiple;
            x |= (i << k);
            ans = max(ans, x);
        }
        
        return ans;
    }
};