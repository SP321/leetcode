class Solution {
public:
    int getDigits(int num) {
        int count = 0;
        while (num) {
            count++;
            num /= 10;
        }
        return count;
    }
    long long findTheArrayConcVal(vector<int>& nums) {
        long long ans = 0;
        while (!nums.empty()) {
            if (nums.size() == 1) {
                ans += nums[0];
                nums.clear();
            } else {
                int first = nums.front();
                int last = nums.back();
                int factor = pow(10, getDigits(last));
                ans += (1ll)*first * factor + last;
                nums.erase(nums.begin());
                nums.pop_back();
            }
        }
        return ans;
    }
};