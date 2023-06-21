class Solution {
public:
    long long minCost(vector<int>& nums, vector<int>& cost) {
        int left = 1, right = 1e6;
        long long ans = LLONG_MAX;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            long long c1 = 0, c2 = 0;
            
            for (int i = 0; i < nums.size(); ++i) {
                c1 += 1LL*abs(nums[i] - mid) * cost[i];
                c2 += 1LL*abs(nums[i] - (mid + 1)) * cost[i];
            }
            
            if (c1 < c2) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
            
            ans = min(ans, min(c1, c2));
        }
        
        return ans;
    }
};