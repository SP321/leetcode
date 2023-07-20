class Solution {
public:
    void sortColors(vector<int>& nums) {
        int p0 = 0, curr = 0;
        int p2 = nums.size() - 1;

        while (curr <= p2) {
            if (nums[curr] == 0) {
                swap(nums[curr++], nums[p0++]);
            } else if (nums[curr] == 2) {
                swap(nums[curr], nums[p2--]);
            } else {
                curr++;
            }
        }
    }
};