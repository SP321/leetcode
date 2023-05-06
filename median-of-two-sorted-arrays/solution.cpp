class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();
        if (m > n)
            return findMedianSortedArrays(nums2, nums1);
        int total = m + n;
        int low = 0;
        int high = m;
        double result = 0.0;
        while (low <= high) {
            int i = low + (high - low) / 2;
            int j = (total + 1) / 2 - i;

            int l1 = (i > 0) ? nums1[i - 1] : INT_MIN;
            int r1 = (i < m) ? nums1[i] : INT_MAX;
            int l2 = (j > 0) ? nums2[j - 1] : INT_MIN;
            int r2 = (j < n) ? nums2[j] : INT_MAX;

            if (l1 <= r2 && l2 <= r1) {
                if (total % 2 == 0)
                    result = (max(l1, l2) + min(r1, r2)) / 2.0;
                else
                    result = max(l1, l2);
                break;
            }
            else if (l1 > r2)
                high = i - 1;
            else
                low = i + 1;
        }
        return result;
    }
};
