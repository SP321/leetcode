class Solution {
public:
    int sumOfPower(std::vector<int>& nums) {
        const int md = 1e9+7;
        uint64_t ans = 0;
        std::sort(nums.begin(), nums.end());
        uint64_t factor = 0;
        
        for (uint64_t v : nums) {
            uint64_t square = (v * v)%md;
            ans += (square * factor) % md + (square * v) % md;
            ans %= md;
            factor *= 2;
            factor += v;
            factor %= md;
        }
        
        return ans % md;
    }
};