class Solution {
public:
    vector<bool> isArraySpecial(vector<int>& nums, vector<vector<int>>& queries) {
        vector<int> pref{0};
        for (int i = 1; i < nums.size(); ++i)
            pref.push_back(pref.back() + (nums[i - 1] % 2 == nums[i] % 2));
        vector<bool> ans;
        for (const auto &q : queries)
            ans.push_back(pref[q[0]] == pref[q[1]]);
        return ans;
    }
};