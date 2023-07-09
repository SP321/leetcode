class Solution {
public:
    int alternatingSubarray(vector<int>& nums) {
        int n = nums.size();
        vector<int> x(n - 1);

        for (int i = 1; i < n; i++) {
            x[i - 1] = nums[i] - nums[i - 1];
        }

        int max_len = 0;
        int count = 0;

        for (int i = 0; i < n - 1; ++i) {
            if (count > 0 && x[i] == -x[i - 1] && abs(x[i]) == 1) {
                count++;
            } else if (x[i] == 1) {
                count = 1;
            } else {
                count = 0;
            }
            max_len = max(max_len, count);
        }

        return max_len > 0 ? max_len + 1 : -1;
    }
};