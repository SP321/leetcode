class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        @cache
        def dp(i, j, k, cycle=0):
            if k == 0: return 0
            if j - i + 1 < k * 2 - 1: return -inf
            return max(dp(i + cycle, j - 2, k - 1) + slices[j], dp(i, j - 1, k))
        return dp(0, len(slices) - 1, len(slices) // 3, 1)