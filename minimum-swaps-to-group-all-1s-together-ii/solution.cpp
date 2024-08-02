class Solution {
public:
    int minSwaps(vector<int>& nums) {
        int c = 0;
        for (int &x:nums)
            c+=x;
        int n = nums.size();
        int i = 0;
        int cur = 0;
        int ans = c;
        for (int j = 0; j < n * 2; ++j) {
            cur += nums[j % n];
            while (j - i + 1 > c) {
                cur -= nums[i % n];
                i++;
            }
            if (j - i + 1 == c) {
                ans = min(ans, c - cur);
            }
        }
        return ans;
    }
};