class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int ans = nums[0];
        int mi = 1, ma = 1;
        for (int i : nums) {
            int prev_ma = ma; 
            ma = max({i * ma, i * mi, i});
            mi = min({i * prev_ma, i * mi, i});
            ans = max(ans, ma);
        }
        return ans;
    }
};