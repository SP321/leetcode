std::unordered_set<int> s = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97};
class Solution {
public:
    int maximumPrimeDifference(std::vector<int>& nums) {
        int a = -1, b = -1;
        for (int i = 0; i < nums.size(); ++i) {
            if (s.find(nums[i]) != s.end()) {
                if (a == -1) {
                    a = i;
                }
                b = i;
            }
        }
        return  b - a;
    }
};