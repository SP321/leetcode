class Solution {
public:
    int maximumScore(vector<int>& nums, int k) {
        int n = nums.size();
        int left = k, right = k;
        int curmin = nums[k];
        int ans = nums[k];
        
        while (left > 0 || right < n - 1) {
            if (left == 0) {
                right++;
                curmin = min(curmin, nums[right]);
            } else if (right == n - 1 || nums[left - 1] >= nums[right + 1]) {
                left--;
                curmin = min(curmin, nums[left]);
            } else {
                right++;
                curmin = min(curmin, nums[right]);
            }
            
            ans = max(ans, curmin * (right - left + 1));
        }
        return ans;
    }
};