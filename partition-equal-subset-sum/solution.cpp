class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int total_sum = accumulate(nums.begin(), nums.end(), 0);
        
        if (total_sum % 2 == 1) {
            return false;
        }

        unordered_set<int> s, s_next;
        s.insert(0);
        int target = total_sum / 2;

        for (int num : nums) {
            s_next = s;

            for (int t : s) {
                int next = t + num;
                s_next.insert(next);

                if (next == target) {
                    return true;
                }
            }

            s = s_next;
        }
        
        return false;
    }
};