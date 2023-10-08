class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n=len(nums1)
        m=len(nums2)
        @cache
        def dfs(i, j,taken=False):
            if i >= n or j >= m:
                if not taken:
                    return float("-inf")
                return 0
            take_both = nums1[i] * nums2[j] + max(0, dfs(i+1, j+1,True))
            skip_i = dfs(i+1, j, taken)
            skip_j = dfs(i, j+1, taken)
            return max(take_both, skip_i, skip_j)
        return dfs(0, 0)