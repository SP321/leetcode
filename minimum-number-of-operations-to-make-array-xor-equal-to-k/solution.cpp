class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        return __builtin_popcount(accumulate(nums.begin(), nums.end(), k,bit_xor<int>()));
    }
};