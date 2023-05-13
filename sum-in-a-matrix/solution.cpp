class Solution {
public:
    int matrixSum(vector<vector<int>>& nums) {
        int n = nums.size();
        int m = nums[0].size();

        for (int i = 0; i < n; i++) {
            sort(nums[i].begin(), nums[i].end());
        }

        int sum = 0;

        for (int i = 0; i < m; i++) {
            int maxElement = nums[0][i];
            for (int j = 1; j < n; j++) {
                maxElement = max(maxElement, nums[j][i]);
            }
            sum += maxElement;
        }

        return sum;
    }
};