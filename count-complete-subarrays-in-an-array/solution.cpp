class Solution {
public:
    int countCompleteSubarrays(std::vector<int>& nums) {
        int n = nums.size();
        set<int> s(nums.begin(), nums.end());
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            set<int> a;
            for (int j = i; j < n; ++j) {
                a.insert(nums[j]);
                if (a.size() == s.size()) {
                    ++ans;
                }
            }
        }
        return ans;
    }
};