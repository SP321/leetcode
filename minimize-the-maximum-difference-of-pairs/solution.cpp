class Solution {
public:
    vector<int> nums;
    vector<int> diffs;
    vector<int> sorted_diffs;
    int n, p;
    
    int minimizeMax(vector<int>& nums, int p) {
        if (p == 0) return 0;
        
        this->nums = nums;
        this->p = p;
        
        sort(this->nums.begin(), this->nums.end());
        n = this->nums.size();
        
        for (int i = 1; i < n; ++i) {
            diffs.push_back(this->nums[i] - this->nums[i - 1]);
        }
        sorted_diffs = diffs;
        sort(sorted_diffs.begin(), sorted_diffs.end());
        
        int low = 0, high = n - 2;
        while (low <= high) {
            int mid = (low + high) / 2;
            if (can_form_pairs(sorted_diffs[mid])) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return sorted_diffs[low];
    }
    
    bool can_form_pairs(int mid_diff) {
        set<int> used;
        int count = 0;
        int i = 0;
        while (i < n - 1) {
            if (diffs[i] <= mid_diff) {
                i++;
                count++;
                if (count == p) {
                    return 1;
                }
            }
            i++;
        }
        return 0;
    }
};