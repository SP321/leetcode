class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        total = m + n
        low = 0
        high = m
        result = 0.0
        while low <= high:
            i = low + (high - low) // 2
            j = (total + 1) // 2 - i

            l1 = nums1[i - 1] if i > 0 else float('-inf')
            r1 = nums1[i] if i < m else float('inf')
            l2 = nums2[j - 1] if j > 0 else float('-inf')
            r2 = nums2[j] if j < n else float('inf')

            if l1 <= r2 and l2 <= r1:
                if total % 2 == 0:
                    result = (max(l1, l2) + min(r1, r2)) / 2.0
                else:
                    result = max(l1, l2)
                break
            elif l1 > r2:
                high = i - 1
            else:
                low = i + 1
        return result