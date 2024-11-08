class Solution {
public:
    int splitArray(vector<int>& nums, int k) {
        auto check = [&](int sm) -> int {
            int count = 1, currentSum = 0;
            for (int x : nums) {
                if (x > sm) return -1;
                if (currentSum + x > sm) {
                    currentSum = x;
                    count++;
                } else {
                    currentSum += x;
                }
            }
            return count > k ? -1 : 0;
        };

        int left = *std::max_element(nums.begin(), nums.end());
        int right = std::accumulate(nums.begin(), nums.end(), 0);
        int pos = right;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (check(mid) == 0) {
                pos = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return pos;
    }
};