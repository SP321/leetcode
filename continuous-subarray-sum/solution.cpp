class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> c;
        c[0] = -1;
        int cur = 0;
        for (int i = 0; i < nums.size(); ++i) {
            cur += nums[i];
            int mod = cur % k;
            if (c.find(mod) != c.end()) {
                if (i - c[mod] > 1) {
                    return true;
                }
            } else {
                c[mod] = i;
            }
        }
        return false;
    }
};